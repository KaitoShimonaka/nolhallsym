from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import spglib

from nolhallsym.magnetic_point_group import MagneticPointGroup
import re

from importlib.resources import files


TABLE_FOR_MSG_MPG_PATH = files('nolhallsym.assets').joinpath('table_for_MSG_MPG.txt')
_TABLE_ROWS_CACHE: list[dict[str, str]] | None = None


@dataclass(frozen=True)
class UniMpgGroup:
	UNI_MPG_symb: MagneticPointGroup
	BNS_MSG_num_list: list[str]


def _load_table_for_msg_mpg_rows() -> list[dict[str, str]]:
	global _TABLE_ROWS_CACHE

	if _TABLE_ROWS_CACHE is not None:
		return _TABLE_ROWS_CACHE

	if not TABLE_FOR_MSG_MPG_PATH.exists():
		raise FileNotFoundError(f"Table file not found: {TABLE_FOR_MSG_MPG_PATH}")

	rows: list[dict[str, str]] = []
	with TABLE_FOR_MSG_MPG_PATH.open("r", encoding="utf-8") as handle:
		for line in handle:
			stripped = line.strip()
			if not stripped or stripped.startswith("BNS_MSG_num"):
				continue

			parts = stripped.split()
			if len(parts) < 6:
				continue

			rows.append(
				{
					"BNS_MSG_num": parts[0],
					"BNS_MSG_symb": parts[1],
					"OG_MSG_num": parts[2],
					"OG_MSG_symb": parts[3],
					"UNI_MSG_symb": parts[4],
					"UNI_MPG_symb": parts[5],
					"FSG->MSG_transform": " ".join(parts[6:]) if len(parts) > 6 else "",
				}
			)

	_TABLE_ROWS_CACHE = rows
	return rows


def _find_table_row_by_bns_msg_num(bns_msg_num: str) -> dict[str, str]:
	target = str(bns_msg_num).strip()
	for row in _load_table_for_msg_mpg_rows():
		if row["BNS_MSG_num"] == target:
			return row
	raise KeyError(f"BNS_MSG_num not found in table: {bns_msg_num}")

def uni_2_mpg_enum(uni_num: int) -> MagneticPointGroup:
	"""
	UNI symbol の番号から対応する MagneticPointGroup enum を返す。
	"""
	msg_type = spglib.get_magnetic_spacegroup_type(uni_num)
	bns_msg_num = msg_type.bns_number
	row = _find_table_row_by_bns_msg_num(bns_msg_num)
	uni_mpg_symb = row["UNI_MPG_symb"]
	return MagneticPointGroup.from_rawstr(uni_mpg_symb)


def read_uni_msg_symb(bns_msg_num: str) -> str:
	"""BNS_MSG_num から UNI_MSG_symb を返す。"""
	return _find_table_row_by_bns_msg_num(bns_msg_num)["UNI_MSG_symb"]


def read_uni_mpg_symb(bns_msg_num: str) -> str:
	"""BNS_MSG_num から UNI_MPG_symb を返す。"""
	return _find_table_row_by_bns_msg_num(bns_msg_num)["UNI_MPG_symb"]


def read_uni_mpg_groups() -> list[UniMpgGroup]:
	"""
	table_for_MSG_MPG.txt を読み、
	UNI_MPG_symb ごとに対応する全 BNS_MSG_num をまとめた dataclass のリストを返す。
	"""
	grouped_rows: dict[MagneticPointGroup, list[str]] = {}
	uni_mpg_order: list[MagneticPointGroup] = []

	for row in _load_table_for_msg_mpg_rows():
		uni_mpg_symb = MagneticPointGroup.from_rawstr(row["UNI_MPG_symb"])
		bns_msg_num = row["BNS_MSG_num"]

		if uni_mpg_symb not in grouped_rows:
			grouped_rows[uni_mpg_symb] = []
			uni_mpg_order.append(uni_mpg_symb)

		grouped_rows[uni_mpg_symb].append(bns_msg_num)

	return [
		UniMpgGroup(
			UNI_MPG_symb=uni_mpg_symb,
			BNS_MSG_num_list=grouped_rows[uni_mpg_symb],
		)
		for uni_mpg_symb in uni_mpg_order
	]


def find_uni_number_by_bns(target_bns: str):
	"""
	BNS number (例: "47.252") から UNI number (1〜1651) を逆引きする
	"""
	for uni in range(1, 1652):
		msg_type = spglib.get_magnetic_spacegroup_type(uni)

		if msg_type.bns_number == target_bns:
			return uni
	return None

def msg_symbol_to_latex(bns_symbol: str) -> str:
    """
    BNS_MSG_symbの文字列をLaTeXの数式表記に変換する関数
    
    Parameters:
        bns_symbol (str): BNS表記の磁気空間群シンボル (例: "P_c-42_1c")
        
    Returns:
        str: LaTeXで正しく描画できる数式文字列 (例: "$P_{c}\bar{4}2_{1}c$")
    """
    
    # 1. 空間反転（- とその直後の1つの数字）を \bar{数字} に置換
    # 例: "P-4" -> "P\bar{4}", "Pm-3m" -> "Pm\bar{3}m"
    latex_str = re.sub(r'-(\d)', r'\\bar{\1}', bns_symbol)
    
    # 2. 下付き文字（_ とその直後の1つの英数字）を _{文字} に置換
    # 例: "P_c2_1" -> "P_{c}2_{1}"
    latex_str = re.sub(r'_([a-zA-Z0-9])', r'_{\1}', latex_str)
    
    # LaTeXの数式モード（$$）で囲んで出力
    return f"${latex_str}$"
