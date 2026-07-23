from dataclasses import dataclass
import sympy as sp
from typing import Self
from nolhallsym.conductivity_component import ConductivityComponent
from nolhallsym.get_operations import Operation, get_magnetic_point_group
from nolhallsym.tensor_index import ABC, SIGMA_VARS

from pathlib import Path
from typing import Any
import yaml
from importlib.resources import files

YAML_DIR = files('nolhallsym.assets').joinpath('yaml')

@dataclass
class nlh:
    tensor : list[sp.Matrix]
    uni_num : int
    nlhe_type : ConductivityComponent

    @classmethod
    def solve_nullspace(
        cls, 
        uni_num: int,
        operations: list[Operation], 
        nlhe_type: ConductivityComponent,
    ) -> Self:
        I = sp.eye(18)
        equations_list = []

        for op in operations:
            Du = sp.Matrix(op.rotation) * op.time_rev_int()

            is_time_reversed = op.time_reversal

            if nlhe_type == ConductivityComponent.BCD and is_time_reversed:
                eta_i = -1
            else:
                eta_i = 1

            M_18x18 = sp.zeros(18, 18)

            for row_idx in range(18):
                abc_out = ABC.num_2_index(row_idx)
                a, b, c = abc_out.a, abc_out.b, abc_out.c

                for col_idx in range(18):
                    abc_in = ABC.num_2_index(col_idx)
                    ap, bp, cp = abc_in.a, abc_in.b, abc_in.c

                    if bp == cp:
                        val = Du[a, ap] * Du[b, bp] * Du[c, cp]
                    else:
                        val = Du[a, ap] * Du[b, bp] * Du[c, cp] + \
                            Du[a, ap] * Du[b, cp] * Du[c, bp]

                    M_18x18[row_idx, col_idx] = val

            condition_block = I - eta_i * M_18x18

            for i in range(18):
                equations_list.append(condition_block.row(i))

        if nlhe_type == ConductivityComponent.NLD:
            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        idx1 = ABC(a, min(b, c), max(b, c)).index_2_num()
                        idx2 = ABC(b, min(a, c), max(a, c)).index_2_num()

                        if idx1 != idx2:
                            row = sp.zeros(1, 18)
                            row[0, idx1] = 1
                            row[0, idx2] = -1
                            equations_list.append(row)

        if nlhe_type in (ConductivityComponent.BCD, ConductivityComponent.INTER_QMD):
            for a in range(3):
                idx = ABC(a, a, a).index_2_num()
                row = sp.zeros(1, 18)
                row[0, idx] = 1
                equations_list.append(row)

        if nlhe_type == ConductivityComponent.BCD:
            # sigma^{xyz} + sigma^{yzx} + sigma^{zxy} = 0
            idx_1 = ABC(0, 1, 2).index_2_num()
            idx_2 = ABC(1, 2, 0).index_2_num()
            idx_3 = ABC(2, 0, 1).index_2_num()
            row = sp.zeros(1, 18)
            row[0, idx_1] = 1
            row[0, idx_2] = 1
            row[0, idx_3] = 1
            equations_list.append(row)

            # sigma^{aab} = -1/2 sigma^{baa} for a != b
            for i in range(3):
                for j in range(3):
                    if i != j:
                        idx_1 = ABC(i, i, j).index_2_num()
                        idx_2 = ABC(j, i, i).index_2_num()
                        row = sp.zeros(1, 18)
                        row[0, idx_1] = 2
                        row[0, idx_2] = 1
                        equations_list.append(row)
                


        A = sp.Matrix(equations_list)
        basis_vectors = A.nullspace()

        return cls(tensor=basis_vectors, uni_num=uni_num, nlhe_type=nlhe_type)
    
    @classmethod
    def calc(cls, uni_num: int, nlhe_type: ConductivityComponent) -> Self:
        """
        UNI symbol の番号と成分を指定して、テンソル基底リストを計算する。
        """
        operations = get_magnetic_point_group(uni_num)
        return cls.solve_nullspace(uni_num, operations, nlhe_type)
    
    @classmethod
    def read(cls, uni_num: int, nlhe_type: ConductivityComponent) -> Self:
        """
        保存済み YAML から特定の成分のテンソル基底リストを読み出す。

        Args:
            uni_num: UNI symbol の番号。
            nlhe_type: 読み込む成分 (ConductivityComponent enum または文字列)。

        Returns:
            指定した成分の basis_vectors を SymPy Matrix の list として返す。
        """
        file_path = _tensor_cache_path(uni_num)
        if not file_path.exists():
            print(f"YAML file for UNI {uni_num} not found. Calculating...")
            return cls.calc(uni_num, nlhe_type)

        data = _load_data(file_path)
        component_name = _component_name(nlhe_type)

        if "components" not in data or component_name not in data["components"]:
            raise ValueError(f"Component '{component_name}' not found for UNI {uni_num}")

        component_data = data["components"][component_name]
        return cls(tensor=[_deserialize_matrix_vector(vec) for vec in component_data["basis_vectors"]], uni_num=uni_num, nlhe_type=nlhe_type)
    
    def format_table_I(self) -> str:
        """
        nullspaceの基底ベクトルリストを受け取り、
        論文 Table I の形式 (b=c に限った 3x3 行列) で出力する関数。
        """
        target_indices = [
            ABC(0, 0, 0).index_2_num(),
            ABC(0, 1, 1).index_2_num(),
            ABC(0, 2, 2).index_2_num(),
            ABC(1, 0, 0).index_2_num(),
            ABC(1, 1, 1).index_2_num(),
            ABC(1, 2, 2).index_2_num(),
            ABC(2, 0, 0).index_2_num(),
            ABC(2, 1, 1).index_2_num(),
            ABC(2, 2, 2).index_2_num()
        ]

        names = [
            "xxx", "xyy", "xzz",
            "yxx", "yyy", "yzz",
            "zxx", "zyy", "zzz"
        ]

        basis_vectors = self.tensor

        if not basis_vectors:
            return _build_matrix_string(["0"] * 9)

        k = len(basis_vectors)
        V_rows = []
        for idx in target_indices:
            row = sp.Matrix(1, k, [vec[idx] for vec in basis_vectors])
            V_rows.append(row)

        priority_order = [8, 7, 6, 5, 4, 3, 2, 1, 0]

        basis_indices = []
        for i in priority_order:
            row_i = V_rows[i]
            if row_i.is_zero_matrix:
                continue

            current_rows = [V_rows[j].tolist()[0] for j in basis_indices]
            current_rows.append(row_i.tolist()[0])
            test_mat = sp.Matrix(current_rows)

            if test_mat.rank() > len(basis_indices):
                basis_indices.append(i)

        result_strs = []
        if not basis_indices:
            return _build_matrix_string(["0"] * 9)

        B_mat = sp.Matrix([V_rows[j].tolist()[0] for j in basis_indices])
        A = B_mat * B_mat.T

        for i in range(9):
            row_i = V_rows[i]
            if row_i.is_zero_matrix:
                result_strs.append("0")
            else:
                b = B_mat * row_i.T
                coeffs = A.LUsolve(b)

                terms = []
                for c_val, b_idx in zip(coeffs, basis_indices):
                    if c_val == 0:
                        continue

                    c_val = sp.simplify(c_val)
                    if c_val == 1:
                        terms.append(names[b_idx])
                    elif c_val == -1:
                        terms.append("-" + names[b_idx])
                    else:
                        terms.append(f"{sp.sstr(c_val)}{names[b_idx]}")

                if not terms:
                    result_strs.append("0")
                else:
                    expr_str = terms[0]
                    for term in terms[1:]:
                        if term.startswith("-"):
                            expr_str += " - " + term[1:]
                        else:
                            expr_str += " + " + term
                    result_strs.append(expr_str)

        return _build_matrix_string(result_strs)
    
    def format_table_nwad104(self) -> str:
        """
        nullspaceの基底ベクトルリストを受け取り、
        論文 Table S10 の形式 (全成分の 3x3x3 テンソル) で出力する関数。
        優先順位: 添え字が若い方 (xxx -> xxy -> xxz -> ... -> zzz) を優先
        """
        names_18 = [
            "xxx", "xxy", "xxz", "xyy", "xyz", "xzz",
            "yxx", "yxy", "yxz", "yyy", "yyz", "yzz",
            "zxx", "zxy", "zxz", "zyy", "zyz", "zzz"
        ]

        basis_vectors = self.tensor

        if not basis_vectors:
            return _build_table_S10_string(["0"] * 18)

        k = len(basis_vectors)
        V_rows = []
        for idx in range(18):
            row = sp.Matrix(1, k, [vec[idx] for vec in basis_vectors])
            V_rows.append(row)

        priority_order = list(range(18))

        basis_indices = []
        for i in priority_order:
            row_i = V_rows[i]
            if row_i.is_zero_matrix:
                continue

            current_rows = [V_rows[j].tolist()[0] for j in basis_indices]
            current_rows.append(row_i.tolist()[0])
            test_mat = sp.Matrix(current_rows)

            if test_mat.rank() > len(basis_indices):
                basis_indices.append(i)

        result_strs = []
        if not basis_indices:
            return _build_table_S10_string(["0"] * 18)

        B_mat = sp.Matrix([V_rows[j].tolist()[0] for j in basis_indices])
        A = B_mat * B_mat.T

        for i in range(18):
            row_i = V_rows[i]
            if row_i.is_zero_matrix:
                result_strs.append("0")
            else:
                b = B_mat * row_i.T
                coeffs = A.LUsolve(b)

                terms = []
                for c_val, b_idx in zip(coeffs, basis_indices):
                    if c_val == 0:
                        continue

                    c_val = sp.simplify(c_val)
                    if c_val == 1:
                        terms.append(names_18[b_idx])
                    elif c_val == -1:
                        terms.append("-" + names_18[b_idx])
                    else:
                        terms.append(f"{sp.sstr(c_val)}{names_18[b_idx]}")

                if not terms:
                    result_strs.append("0")
                else:
                    expr_str = terms[0]
                    for term in terms[1:]:
                        if term.startswith("-"):
                            expr_str += " - " + term[1:]
                        else:
                            expr_str += " + " + term
                    result_strs.append(expr_str)

        return _build_table_S10_string(result_strs)
    
    def contain_after_2_index_is_same(self) -> bool:
        """
        基底ベクトルのリストの中に、
        テンソル成分 σ^{a;bc} のうち b = c となる要素が1つでも非ゼロであるベクトルが存在するか判定する。
        """
        target_indices = [ABC(a, b, b).index_2_num() for a in range(3) for b in range(3)]

        for vector in self.tensor:
            if any(vector[idx] != 0 for idx in target_indices):
                return True

        return False
    
    def is_nonzero(self) -> bool:
        """
        基底ベクトルのリストの中に、非ゼロのベクトルが1つでも存在するか判定する。
        """
        for vector in self.tensor:
            if any(component != 0 for component in vector):
                return True

        return False
    
    def allow_transvese_component(self) -> tuple[bool, bool, bool]:
        """
        基底ベクトルのリストの中に、sigma_aaa の成分があるかを判定
        """
        has_xxx = any(vec[ABC(0, 0, 0).index_2_num()] != 0 for vec in self.tensor)
        has_yyy = any(vec[ABC(1, 1, 1).index_2_num()] != 0 for vec in self.tensor) 
        has_zzz = any(vec[ABC(2, 2, 2).index_2_num()] != 0 for vec in self.tensor)
        return has_xxx, has_yyy, has_zzz
    
    def _build_component_payload(self) -> dict[str, Any]:
        basis_vectors = self.tensor
        return {
            "free_degree": len(basis_vectors),
            "basis_vectors": [_serialize_matrix_vector(vec) for vec in basis_vectors],
            "constraints": [_format_constraint(vec) for vec in basis_vectors],
        }
    
    def save_img(self):
        """
        基底ベクトルのリストを画像として保存する。
        """
        import matplotlib.pyplot as plt
        from matplotlib import rcParams

        rcParams["text.usetex"] = True
        rcParams["font.size"] = 36
        rcParams["font.family"] = "serif"
        rcParams["font.serif"] = ["Computer Modern Roman"]
        rcParams["mathtext.fontset"] = "cm"

        names_18 = [
            "xxx", "xxy", "xxz", "xyy", "xyz", "xzz",
            "yxx", "yxy", "yxz", "yyy", "yyz", "yzz",
            "zxx", "zxy", "zxz", "zyy", "zyz", "zzz"
        ]
        basis_vectors = self.tensor
        target_indices = list(range(18))

        if not basis_vectors:
            result_strs_18 = [r"0"] * 18
        else:
            k = len(basis_vectors)
            V_rows = []
            for idx in target_indices:
                row = sp.Matrix(1, k, [vec[idx] for vec in basis_vectors])
                V_rows.append(row)

            basis_indices: list[int] = []
            for i in range(18):
                row_i = V_rows[i]
                if row_i.is_zero_matrix:
                    continue

                current_rows = [V_rows[j].tolist()[0] for j in basis_indices]
                current_rows.append(row_i.tolist()[0])
                test_mat = sp.Matrix(current_rows)

                if test_mat.rank() > len(basis_indices):
                    basis_indices.append(i)

            if not basis_indices:
                result_strs_18 = [r"0"] * 18
            else:
                B_mat = sp.Matrix([V_rows[j].tolist()[0] for j in basis_indices])
                A = B_mat * B_mat.T
                result_strs_18 = []

                for i in range(18):
                    row_i = V_rows[i]
                    if row_i.is_zero_matrix:
                        result_strs_18.append(r"0")
                        continue

                    b = B_mat * row_i.T
                    coeffs = A.LUsolve(b)

                    terms = []
                    for c_val, b_idx in zip(coeffs, basis_indices):
                        if c_val == 0:
                            continue

                        c_val = sp.simplify(c_val)
                        name = names_18[b_idx]
                        if c_val == 1:
                            terms.append(name)
                        elif c_val == -1:
                            terms.append("-" + name)
                        else:
                            terms.append(f"{sp.latex(c_val)}{name}")

                    if not terms:
                        result_strs_18.append(r"0")
                    else:
                        expr_str = terms[0]
                        for term in terms[1:]:
                            if term.startswith("-"):
                                expr_str += " - " + term[1:]
                            else:
                                expr_str += " + " + term
                        result_strs_18.append(expr_str)

        raw_to_canonical_indices = []
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    raw_to_canonical_indices.append(ABC(a, min(b, c), max(b, c)).index_2_num())

        result_strs = [result_strs_18[idx] for idx in raw_to_canonical_indices]

        latex_rows = []
        for b in (0, 1, 2):
            row_entries = []
            for a in range(3):
                for c in range(3):
                    idx = a * 9 + b * 3 + c
                    value = result_strs[idx]
                    row_entries.append(value)
            latex_rows.append(" & ".join(row_entries))

        latex_body = r" \\ ".join(latex_rows)
        latex_image = (
            r"$\left[\begin{array}{ccc|ccc|ccc}"
            + latex_body
            + r"\end{array}\right]$"
        )

        fig, ax = plt.subplots(figsize=(10, 3))
        ax.axis("off")
        ax.text(
            0.5,
            0.5,
            latex_image,
            ha="center",
            va="center",
            fontsize=36,
        )

        fig.tight_layout(pad=0.2)
        output_path = Path.cwd() / f"tensor_{self.uni_num}_{self.nlhe_type.debug_name()}.png"
        fig.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.close(fig)

        return output_path
    
    @classmethod
    def all_independent(cls) -> Self:
        """
        すべてのテンソル成分が独立である場合の nlh インスタンスを返す。
        """
        basis_vectors = [sp.eye(18).row(i) for i in range(18)]
        return cls(tensor=basis_vectors, uni_num=0, nlhe_type=ConductivityComponent.EXAMPLE)

    
# def write_1651() -> list[Path]:
#     """
#     1〜1651 の UNI symbol について、各 ConductivityComponent のテンソル形を計算し、
#     assets/yaml/uni_XXXX.yaml に保存する。

#     戻り値:
#         保存した YAML ファイルのパス一覧。
#     """
#     saved_paths: list[Path] = []

#     for uni_num in range(1, 1652):
#         operations = get_magnetic_point_group(uni_num)
#         payload: dict[str, Any] = {
#             "uni_number": uni_num,
#             "components": {},
#         }

#         for component in ConductivityComponent:
#             basis_vectors = nlh.solve_nullspace(uni_num, operations, component)
#             payload["components"][_component_name(component)] = basis_vectors._build_component_payload()

#         file_path = _tensor_cache_path(uni_num)
#         _dump_data(file_path, payload)
#         saved_paths.append(file_path)

#     return saved_paths

def _build_matrix_string(result_strs: list[str]) -> str:
    """ 3x3 行列の文字列として綺麗に整形する """
    col_widths = [0, 0, 0]
    for row in range(3):
        for col in range(3):
            width = len(result_strs[row * 3 + col])
            if width > col_widths[col]:
                col_widths[col] = width

    lines = []
    lines.append("(")
    for row in range(3):
        row_str = "  "
        for col in range(3):
            val = result_strs[row * 3 + col]
            row_str += val.ljust(col_widths[col])
            if col < 2:
                row_str += "  "
        lines.append(row_str)
    lines.append(")")
    return "\n".join(lines)


def _build_table_S10_string(result_strs_18: list[str]) -> str:
    """ 3x3 行列を3つ並べた (Table S10) 文字列として綺麗に整形する """
    target_grid = [
        [0, 1, 2, 6, 7, 8, 12, 13, 14],
        [1, 3, 4, 7, 9, 10, 13, 15, 16],
        [2, 4, 5, 8, 10, 11, 14, 16, 17]
    ]

    col_widths = [0] * 9
    for row in range(3):
        for col in range(9):
            idx = target_grid[row][col]
            width = len(result_strs_18[idx])
            if width > col_widths[col]:
                col_widths[col] = width

    lines = []
    lines.append("(")
    for row in range(3):
        row_str = "  "
        for col in range(9):
            idx = target_grid[row][col]
            val = result_strs_18[idx]
            row_str += val.ljust(col_widths[col])
            if col < 8:
                row_str += "  "
        lines.append(row_str)
    lines.append(")")
    return "\n".join(lines)

def _component_name(component: ConductivityComponent | str) -> str:
    return component.name if isinstance(component, ConductivityComponent) else str(component)


def _serialize_matrix_vector(vec: sp.Matrix) -> list[str]:
    return [sp.sstr(sp.simplify(entry)) for entry in vec]


def _deserialize_matrix_vector(serialized_vec: list[str]) -> sp.Matrix:
    return sp.Matrix([sp.sympify(item) for item in serialized_vec])


def _dump_data(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(data, handle, allow_unicode=True, sort_keys=False)


def _load_data(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle)
    return loaded if loaded is not None else {}


def _tensor_cache_path(uni_num: int) -> Path:
    return YAML_DIR / f"uni_{uni_num:04d}.yaml"

def _format_constraint(vec: sp.Matrix) -> str:
    terms = []
    for coeff, symbol in zip(vec, SIGMA_VARS):
        coeff = sp.simplify(coeff)
        if coeff == 0:
            continue
        terms.append((coeff, symbol))

    if not terms:
        return "0 = 0"

    if len(terms) == 1:
        return str(terms[0][1])

    pivot_coeff, pivot_symbol = terms[0]
    normalized = [(sp.simplify(coeff / pivot_coeff), symbol) for coeff, symbol in terms]

    if len(normalized) == 2:
        ratio = normalized[1][0]
        if ratio == 1:
            return f"{normalized[0][1]} = {normalized[1][1]}"
        if ratio == -1:
            return f"{normalized[0][1]} = -{normalized[1][1]}"
        return f"{normalized[0][1]} = {sp.sstr(ratio)}*{normalized[1][1]}"

    if all(ratio == 1 for ratio, _ in normalized[1:]):
        return " = ".join(str(symbol) for _, symbol in normalized)

    if all(ratio == -1 for ratio, _ in normalized[1:]):
        return f"{normalized[0][1]} = " + " = ".join(f"-{symbol}" for _, symbol in normalized[1:])

    rhs_parts = []
    for ratio, symbol in normalized[1:]:
        if ratio == 1:
            rhs_parts.append(str(symbol))
        elif ratio == -1:
            rhs_parts.append(f"-{symbol}")
        else:
            rhs_parts.append(f"{sp.sstr(ratio)}*{symbol}")

    return f"{normalized[0][1]} = " + " = ".join(rhs_parts)