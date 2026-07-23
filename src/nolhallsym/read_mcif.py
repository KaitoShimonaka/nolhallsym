from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import rcParams
import sympy as sp

from nolhallsym.conductivity_component import ConductivityComponent
from nolhallsym.table_for_MSG_MPG import find_uni_number_by_bns, read_uni_msg_symb, msg_symbol_to_latex
from nolhallsym.nlh_tensor import nlh
from nolhallsym.tensor_index import ABC

import re

@dataclass
class McifAnalysisResult:
    formula : str | None
    bns_number: str | None
    has_ON_halogen: bool

COMPONENTS : str = r"$\left[\begin{array}{ccc|ccc|ccc}xxx & xxy & xxz & yxx & yxy & yxz & zxx & zxy & zxz\\xyx & xyy & xyz & yyx & yyy & yyz & zyx & zyy & zyz\\xzx & xzy & xzz & yzx & yzy & yzz & zzx & zzy & zzz\end{array}\right]$"


def make_tensor_mcif(
        file_path: str,
        output_dir: str | None = None,
    ):
    result = analyze_mcif(file_path)
    if result is None:
        raise ValueError(f"Failed to analyze mcif: {file_path}")
    file_name = Path(file_path).stem
    

    uni_number = find_uni_number_by_bns(result.bns_number)
    msg = read_uni_msg_symb(result.bns_number)
    structure_name = result.formula

    tensors = [
        ("component", nlh.all_independent()),
        ("Drude", nlh.read(uni_number, ConductivityComponent.NLD)),
        ("BCD", nlh.read(uni_number, ConductivityComponent.BCD)),
        ("INTER\ QMD", nlh.read(uni_number, ConductivityComponent.INTER_QMD)),
        ("INTRA\ QMD", nlh.read(uni_number, ConductivityComponent.INTRA_QMD)),
    ]

    rcParams["text.usetex"] = True
    rcParams["font.size"] = 18
    rcParams["font.family"] = "serif"
    rcParams["font.serif"] = ["Computer Modern Roman"]
    rcParams["mathtext.fontset"] = "cm"

    fig = plt.figure(figsize=(12, 8))
    grid = fig.add_gridspec(6, 1, height_ratios=[0.7, 1, 1, 1, 1, 1], hspace=0.55)

    title_ax = fig.add_subplot(grid[0, 0])
    title_ax.axis("off")
    title_ax.text(0.5, 0.7, rf"$\mathrm{{{file_name}}}$.mcif", ha="center", va="center", fontsize=22)
    title_ax.text(
        0.5, 0.2, 
        rf"$\mathrm{{BNS}}: {result.bns_number}$ , $\mathrm{{MSG}}: ${msg_symbol_to_latex(msg)}", 
        ha="center", va="center", fontsize=22
    )


    for row_idx, (component_name, tensor) in enumerate(tensors, start=1):
        ax = fig.add_subplot(grid[row_idx, 0])
        ax.axis("off")

        if row_idx == 1:
            table_tex = COMPONENTS
        else:
            table_tex = _build_tensor_summary_table_tex(tensor)

        ax.text(0.02, 0.5, rf"$\mathrm{{{component_name}}}$", ha="left", va="center", fontsize=20)
        ax.text(0.5, 0.5, table_tex, ha="center", va="center", fontsize=18)

    if output_dir:
        plt.savefig(Path(output_dir) / f"mcif_tensor_{file_name}.pdf", dpi=300, bbox_inches="tight")
    else:
        plt.savefig(f"mcif_tensor_{file_name}.pdf", dpi=300, bbox_inches="tight")


def _build_tensor_summary_table_tex(tensor: nlh) -> str:
    names_18 = [
        "xxx", "xxy", "xxz", "xyy", "xyz", "xzz",
        "yxx", "yxy", "yxz", "yyy", "yyz", "yzz",
        "zxx", "zxy", "zxz", "zyy", "zyz", "zzz"
    ]

    basis_vectors = tensor.tensor
    target_indices = list(range(18))

    if not basis_vectors:
        result_strs_18 = [r"0"] * 18
    else:
        k = len(basis_vectors)
        V_rows = [sp.Matrix(1, k, [vec[idx] for vec in basis_vectors]) for idx in target_indices]

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

    rows = []
    for b in range(3):
        row_entries = []
        for a in range(3):
            for c in range(3):
                idx = a * 9 + b * 3 + c
                row_entries.append(result_strs[idx])
        rows.append(" & ".join(row_entries))

    return rf"$\left[\begin{{array}}{{ccc|ccc|ccc}}{rows[0]}\\{rows[1]}\\{rows[2]}\end{{array}}\right]$"

def check_tensor_mcif(file_path: str):
    result = analyze_mcif(file_path)
    uni_number = find_uni_number_by_bns(result.bns_number)

    nld = nlh.read(uni_number, ConductivityComponent.NLD)
    print('NLD')
    print(nld.format_table_nwad104())
    nld.save_img()
    bcd = nlh.read(uni_number, ConductivityComponent.BCD)
    print('BCD')
    print(bcd.format_table_nwad104())
    bcd.save_img()
    inter_qmd = nlh.read(uni_number, ConductivityComponent.INTER_QMD)
    print('INTER_QMD')
    print(inter_qmd.format_table_nwad104())
    inter_qmd.save_img()
    intra_qmd = nlh.read(uni_number, ConductivityComponent.INTRA_QMD)
    print('INTRA_QMD')
    print(intra_qmd.format_table_nwad104())
    intra_qmd.save_img()


def analyze_mcif(file_path: str) -> McifAnalysisResult:
    """
    外部ライブラリを使用せず、正規表現で .mcif からメタデータを抽出する関数。
    """
    target_elements = {"O", "N", "F", "Cl", "Br", "I", "At", "U", "Th"}
    bns_number = None
    formula = None
    has_target = False

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. BNS番号の抽出
        # 値がクォーテーションで囲まれている場合とそうでない場合の両方に対応
        bns_match = re.search(r'_space_group_magn\.number_BNS\s+["\']?([^"\'\s]+)["\']?', content)
        if bns_match:
            bns_number = bns_match.group(1)

        # 2. 組成式の抽出
        formula_match = re.search(r'_chemical_formula_sum\s+(.+)', content)
        if formula_match:
            # クォーテーションなどの余分な文字を削除
            formula = formula_match.group(1).strip('"\' \r\n')
            
            # 組成式から元素記号のみを抽出 (例: "Mn2 O3" -> ["Mn", "O"])
            # 大文字で始まり、小文字が0〜1回続く文字にマッチ
            elements = set(re.findall(r'[A-Z][a-z]?', formula))
            has_target = not target_elements.isdisjoint(elements)
            
        else:
            # _chemical_formula_sum が無い場合のフォールバック
            # atom_site_type_symbol のループなど、ファイル全体の元素記号らしきものを拾う
            elements = set(re.findall(r'\b[A-Z][a-z]?\b', content))
            has_target = not target_elements.isdisjoint(elements)

        return McifAnalysisResult(bns_number=bns_number, formula=formula, has_ON_halogen=has_target)

    except Exception as e:
        print(f"File reading error: {file_path} - {e}")
        return McifAnalysisResult(bns_number=None, formula=None, has_ON_halogen=False)

import argparse

def main():
    """ターミナルから呼ばれる際の入り口となる関数"""
    # ターミナルでの入力（引数）を受け取る設定
    parser = argparse.ArgumentParser(description="mcifファイルからテンソル形状のPDFを生成します")
    
    # 必須の引数として「ファイルパス」を指定させる
    parser.add_argument("filepath", help="読み込む .mcif ファイルのパス")
    
    # 受け取った引数を解析
    args = parser.parse_args()
    
    print(f"解析を開始します: {args.filepath}")
    
    try:
        # メインの処理（PDF生成）を実行
        make_tensor_mcif(args.filepath)
        print("✅ PDFの生成が完了しました！")
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")

if __name__ == "__main__":
    main()