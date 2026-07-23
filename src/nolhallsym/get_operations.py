import spglib
import sympy as sp

from dataclasses import dataclass
from typing import Any


@dataclass
class Operation:
    # 3x3 の行列 (直交座標系に変換済みの SymPy Matrix)
    rotation: Any
    # 時間反転の有無を示すブール値
    time_reversal: bool

    def time_rev_int(self) -> int:
        """
        time_rev が True の場合は -1、False の場合は 1 を返す
        """
        return -1 if self.time_reversal else 1

    def matrix_element(self, i: int, j: int) -> int:
        """
        回転行列の (i,j) 成分を返す
        """
        return self.rotation[i, j]


def get_magnetic_point_group(
        uni_number: int
) -> list[Operation]:
    """
    指定したUNI numberの磁気空間群から、磁気点群の対称操作を抽出する
    """
    dataset = spglib.get_magnetic_symmetry_from_database(uni_number)

    rotations = dataset['rotations']
    time_reversals = dataset['time_reversals']

    msg_type = spglib.get_magnetic_spacegroup_type(uni_number)
    sg_number = msg_type['number']

    print(f"UNI number {uni_number} の空間群番号: {sg_number}")

    if 143 <= sg_number <= 194:
        M_to_cart = sp.Matrix([
            [1, -sp.Rational(1, 2), 0],
            [0, sp.sqrt(3) / 2, 0],
            [0, 0, 1]
        ])
    else:
        M_to_cart = sp.eye(3)

    M_inv = M_to_cart.inv()

    unique_operations = []
    seen_signatures = set()

    for r, t_rev in zip(rotations, time_reversals):
        signature = tuple(r.flatten()) + (t_rev,)

        if signature not in seen_signatures:
            seen_signatures.add(signature)

            R_frac = sp.Matrix(r)
            R_cart = M_to_cart * R_frac * M_inv

            unique_operations.append(Operation(rotation=R_cart, time_reversal=t_rev))

    return unique_operations
