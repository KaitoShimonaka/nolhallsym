from enum import Enum, auto

class RawMagneticPointGroup(Enum):
    """
    table_for_MSG_MPG.txt に記載されている、冗長な要素を含む磁気点群（Raw MPG）
    """
    MPG_1d1 = auto()
    MPG_1d1p = auto()
    MPG_b1d1 = auto()
    MPG_b1d1p = auto()
    MPG_b1p = auto()
    MPG_2d1 = auto()
    MPG_2d1p = auto()
    MPG_2p = auto()
    MPG_md1 = auto()
    MPG_md1p = auto()
    MPG_mp = auto()
    MPG_2smd1 = auto()
    MPG_2smd1p = auto()
    MPG_2psm = auto()
    MPG_2smp = auto()
    MPG_2psmp = auto()
    MPG_222d1 = auto()
    MPG_222d1p = auto()
    MPG_2p2p2 = auto()
    MPG_22p2p = auto()
    MPG_mm2d1 = auto()
    MPG_mm2d1p = auto()
    MPG_mpm2p = auto()
    MPG_mpmp2 = auto()
    MPG_mmp2p = auto()
    MPG_mmmd1 = auto()
    MPG_mmmd1p = auto()
    MPG_mpmm = auto()
    MPG_mpmpm = auto()
    MPG_mpmpmp = auto()
    MPG_mmmp = auto()
    MPG_mpmmp = auto()
    MPG_mmpm = auto()
    MPG_mmpmp = auto()
    MPG_4d1 = auto()
    MPG_4d1p = auto()
    MPG_4p = auto()
    MPG_b4d1 = auto()
    MPG_b4d1p = auto()
    MPG_b4p = auto()
    MPG_4smd1 = auto()
    MPG_4smd1p = auto()
    MPG_4psm = auto()
    MPG_4smp = auto()
    MPG_4psmp = auto()
    MPG_422d1 = auto()
    MPG_422d1p = auto()
    MPG_4p22p = auto()
    MPG_42p2p = auto()
    MPG_4p2p2 = auto()
    MPG_4mmd1 = auto()
    MPG_4mmd1p = auto()
    MPG_4pmpm = auto()
    MPG_4pmmp = auto()
    MPG_4mpmp = auto()
    MPG_b42md1 = auto()
    MPG_b42md1p = auto()
    MPG_b4p2pm = auto()
    MPG_b4p2mp = auto()
    MPG_b42pmp = auto()
    MPG_b4m2d1 = auto()
    MPG_b4m2d1p = auto()
    MPG_b4pmp2 = auto()
    MPG_b4pm2p = auto()
    MPG_b4mp2p = auto()
    MPG_4smmmd1 = auto()
    MPG_4smmmd1p = auto()
    MPG_4smpmm = auto()
    MPG_4psmmpm = auto()
    MPG_4psmmmp = auto()
    MPG_4psmpmpm = auto()
    MPG_4smmpmp = auto()
    MPG_4psmpmmp = auto()
    MPG_4smpmpmp = auto()
    MPG_3d1 = auto()
    MPG_3d1p = auto()
    MPG_b3d1 = auto()
    MPG_b3d1p = auto()
    MPG_b3p = auto()
    MPG_312d1 = auto()
    MPG_312d1p = auto()
    MPG_312p = auto()
    MPG_321d1 = auto()
    MPG_321d1p = auto()
    MPG_32p1 = auto()
    MPG_32d1 = auto()
    MPG_32d1p = auto()
    MPG_32p = auto()
    MPG_3m1d1 = auto()
    MPG_3m1d1p = auto()
    MPG_3mp1 = auto()
    MPG_31md1 = auto()
    MPG_31md1p = auto()
    MPG_31mp = auto()
    MPG_3md1 = auto()
    MPG_3md1p = auto()
    MPG_3mp = auto()
    MPG_b31md1 = auto()
    MPG_b31md1p = auto()
    MPG_b3p1m = auto()
    MPG_b3p1mp = auto()
    MPG_b31mp = auto()
    MPG_b3m1d1 = auto()
    MPG_b3m1d1p = auto()
    MPG_b3pm1 = auto()
    MPG_b3pmp1 = auto()
    MPG_b3mp1 = auto()
    MPG_b3md1 = auto()
    MPG_b3md1p = auto()
    MPG_b3pm = auto()
    MPG_b3pmp = auto()
    MPG_b3mp = auto()
    MPG_6d1 = auto()
    MPG_6d1p = auto()
    MPG_6p = auto()
    MPG_b6d1 = auto()
    MPG_b6d1p = auto()
    MPG_b6p = auto()
    MPG_6smd1 = auto()
    MPG_6smd1p = auto()
    MPG_6psm = auto()
    MPG_6smp = auto()
    MPG_6psmp = auto()
    MPG_622d1 = auto()
    MPG_622d1p = auto()
    MPG_6p2p2 = auto()
    MPG_6p22p = auto()
    MPG_62p2p = auto()
    MPG_6mmd1 = auto()
    MPG_6mmd1p = auto()
    MPG_6pmpm = auto()
    MPG_6pmmp = auto()
    MPG_6mpmp = auto()
    MPG_b6m2d1 = auto()
    MPG_b6m2d1p = auto()
    MPG_b6pmp2 = auto()
    MPG_b6pm2p = auto()
    MPG_b6mp2p = auto()
    MPG_b62md1 = auto()
    MPG_b62md1p = auto()
    MPG_b6p2pm = auto()
    MPG_b6p2mp = auto()
    MPG_b62pmp = auto()
    MPG_6smmmd1 = auto()
    MPG_6smmmd1p = auto()
    MPG_6smpmm = auto()
    MPG_6psmmpm = auto()
    MPG_6psmmmp = auto()
    MPG_6psmpmpm = auto()
    MPG_6psmpmmp = auto()
    MPG_6smmpmp = auto()
    MPG_6smpmpmp = auto()
    MPG_23d1 = auto()
    MPG_23d1p = auto()
    MPG_mb3d1 = auto()
    MPG_mb3d1p = auto()
    MPG_mpb3p = auto()
    MPG_432d1 = auto()
    MPG_432d1p = auto()
    MPG_4p32p = auto()
    MPG_b43md1 = auto()
    MPG_b43md1p = auto()
    MPG_b4p3mp = auto()
    MPG_mb3md1 = auto()
    MPG_mb3md1p = auto()
    MPG_mpb3pm = auto()
    MPG_mb3mp = auto()
    MPG_mpb3pmp = auto()

    def debug_name(self) -> str:
        """
        Enumから元の文字列（例: "-4'2m'" など）に変換して返す
        """
        # プレフィックス "MPG_" を取り除く
        name_body = self.name[4:]
        
        # 逆変換ルール（b -> -, d -> ., p -> ', s -> /）
        return name_body.replace('b', '-').replace('d', '.').replace('p', "'").replace('s', '/')

    @classmethod
    def from_str(cls, s: str) -> 'MagneticPointGroup':
        """
        元の文字列（例: "m-3m.1'" など）から対応するEnumメンバーを取得する
        """
        # 変換ルール（- -> b, . -> d, ' -> p, / -> s）
        translated = s.replace('-', 'b').replace('.', 'd').replace("'", 'p').replace('/', 's')
        enum_name = f"MPG_{translated}"
        
        try:
            return cls[enum_name]
        except KeyError:
            raise ValueError(f"'{s}' に対応する MagneticPointGroup は定義されていません。")


class MagneticPointGroup(Enum):
    """
    Bilbao Crystallographic Serverの122種類の磁気点群（MPG）
    等価な要素を排除し、一意に定まる122個のみを定義
    """
    MPG_1d1 = auto()
    MPG_1d1p = auto()
    MPG_b1d1 = auto()
    MPG_b1d1p = auto()
    MPG_b1p = auto()
    MPG_2d1 = auto()
    MPG_2d1p = auto()
    MPG_2p = auto()
    MPG_md1 = auto()
    MPG_md1p = auto()
    MPG_mp = auto()
    MPG_2smd1 = auto()
    MPG_2smd1p = auto()
    MPG_2psm = auto()
    MPG_2smp = auto()
    MPG_2psmp = auto()
    MPG_222d1 = auto()
    MPG_222d1p = auto()
    MPG_2p2p2 = auto()
    MPG_mm2d1 = auto()
    MPG_mm2d1p = auto()
    MPG_mpm2p = auto()
    MPG_mpmp2 = auto()
    MPG_mmmd1 = auto()
    MPG_mmmd1p = auto()
    MPG_mpmm = auto()
    MPG_mpmpm = auto()
    MPG_mpmpmp = auto()
    MPG_4d1 = auto()
    MPG_4d1p = auto()
    MPG_4p = auto()
    MPG_b4d1 = auto()
    MPG_b4d1p = auto()
    MPG_b4p = auto()
    MPG_4smd1 = auto()
    MPG_4smd1p = auto()
    MPG_4psm = auto()
    MPG_4smp = auto()
    MPG_4psmp = auto()
    MPG_422d1 = auto()
    MPG_422d1p = auto()
    MPG_4p22p = auto()
    MPG_42p2p = auto()
    MPG_4mmd1 = auto()
    MPG_4mmd1p = auto()
    MPG_4pmpm = auto()
    MPG_4mpmp = auto()
    MPG_b42md1 = auto()
    MPG_b42md1p = auto()
    MPG_b4p2pm = auto()
    MPG_b4p2mp = auto()
    MPG_b42pmp = auto()
    MPG_4smmmd1 = auto()
    MPG_4smmmd1p = auto()
    MPG_4smpmm = auto()
    MPG_4psmmpm = auto()
    MPG_4psmpmpm = auto()
    MPG_4smmpmp = auto()
    MPG_4smpmpmp = auto()
    MPG_3d1 = auto()
    MPG_3d1p = auto()
    MPG_b3d1 = auto()
    MPG_b3d1p = auto()
    MPG_b3p = auto()
    MPG_32d1 = auto()
    MPG_32d1p = auto()
    MPG_32p = auto()
    MPG_3md1 = auto()
    MPG_3md1p = auto()
    MPG_3mp = auto()
    MPG_b3md1 = auto()
    MPG_b3md1p = auto()
    MPG_b3pm = auto()
    MPG_b3pmp = auto()
    MPG_b3mp = auto()
    MPG_6d1 = auto()
    MPG_6d1p = auto()
    MPG_6p = auto()
    MPG_b6d1 = auto()
    MPG_b6d1p = auto()
    MPG_b6p = auto()
    MPG_6smd1 = auto()
    MPG_6smd1p = auto()
    MPG_6psm = auto()
    MPG_6smp = auto()
    MPG_6psmp = auto()
    MPG_622d1 = auto()
    MPG_622d1p = auto()
    MPG_6p22p = auto()
    MPG_62p2p = auto()
    MPG_6mmd1 = auto()
    MPG_6mmd1p = auto()
    MPG_6pmpm = auto()
    MPG_6mpmp = auto()
    MPG_b6m2d1 = auto()
    MPG_b6m2d1p = auto()
    MPG_b6pmp2 = auto()
    MPG_b6pm2p = auto()
    MPG_b6mp2p = auto()
    MPG_6smmmd1 = auto()
    MPG_6smmmd1p = auto()
    MPG_6smpmm = auto()
    MPG_6psmmmp = auto()
    MPG_6psmpmpm = auto()
    MPG_6smmpmp = auto()
    MPG_6smpmpmp = auto()
    MPG_23d1 = auto()
    MPG_23d1p = auto()
    MPG_mb3d1 = auto()
    MPG_mb3d1p = auto()
    MPG_mpb3p = auto()
    MPG_432d1 = auto()
    MPG_432d1p = auto()
    MPG_4p32p = auto()
    MPG_b43md1 = auto()
    MPG_b43md1p = auto()
    MPG_b4p3mp = auto()
    MPG_mb3md1 = auto()
    MPG_mb3md1p = auto()
    MPG_mpb3pm = auto()
    MPG_mb3mp = auto()
    MPG_mpb3pmp = auto()

    def debug_name(self) -> str:
        """
        Enumから元の文字列（例: "-4'2m'" など）に変換して返す
        """
        name_body = self.name[4:]
        return name_body.replace('b', '-').replace('d', '.').replace('p', "'").replace('s', '/')

    @classmethod
    def from_str(cls, s: str) -> 'MagneticPointGroup':
        """
        元の文字列（例: "m-3m.1'" など）から対応するEnumメンバーを取得する
        """
        translated = s.replace('-', 'b').replace('.', 'd').replace("'", 'p').replace('/', 's')
        enum_name = f"MPG_{translated}"
        try:
            return cls[enum_name]
        except KeyError:
            raise ValueError(f"'{s}' (内部名: {enum_name}) は122個のMagneticPointGroupに定義されていません。")

    @classmethod
    def from_raw(cls, raw: RawMagneticPointGroup) -> 'MagneticPointGroup':
        """
        RawMagneticPointGroup（冗長な要素を含む）から、等価で一意な
        MagneticPointGroup（122要素）にマッピングして返す
        """
        # --- 結晶学的な等価性に基づくマッピング規則 ---
        RAW_TO_MPG_MAP = {
            # 222
            RawMagneticPointGroup.MPG_22p2p: "MPG_2p2p2",     # 22'2' -> 2'2'2
            # mm2
            RawMagneticPointGroup.MPG_mmp2p: "MPG_mpm2p",     # mm'2' -> m'm2'
            # mmm
            RawMagneticPointGroup.MPG_mmmp: "MPG_mpmm",       # mmm' -> m'mm
            RawMagneticPointGroup.MPG_mpmmp: "MPG_mpmpm",     # m'mm' -> m'm'm
            RawMagneticPointGroup.MPG_mmpm: "MPG_mpmm",       # mm'm -> m'mm
            RawMagneticPointGroup.MPG_mmpmp: "MPG_mpmpm",     # mm'm' -> m'm'm
            # 422
            RawMagneticPointGroup.MPG_4p2p2: "MPG_4p22p",     # 4'2'2 -> 4'22'
            # 4mm
            RawMagneticPointGroup.MPG_4pmmp: "MPG_4pmpm",     # 4'mm' -> 4'm'm
            # -4m2 -> -42m
            RawMagneticPointGroup.MPG_b4m2d1: "MPG_b42md1",   # -4m2.1 -> -42m.1
            RawMagneticPointGroup.MPG_b4m2d1p: "MPG_b42md1p", # -4m2.1' -> -42m.1'
            RawMagneticPointGroup.MPG_b4pmp2: "MPG_b4p2mp",   # -4'm'2 -> -4'2m'
            RawMagneticPointGroup.MPG_b4pm2p: "MPG_b4p2pm",   # -4'm2' -> -4'2'm
            RawMagneticPointGroup.MPG_b4mp2p: "MPG_b42pmp",   # -4m'2' -> -42'm'
            # 4/mmm
            RawMagneticPointGroup.MPG_4psmmmp: "MPG_4psmmpm", # 4'/mmm' -> 4'/mm'm
            RawMagneticPointGroup.MPG_4psmpmmp: "MPG_4psmpmpm", # 4'/m'mm' -> 4'/m'm'm
            # 312 & 321 -> 32
            RawMagneticPointGroup.MPG_312d1: "MPG_32d1",
            RawMagneticPointGroup.MPG_321d1: "MPG_32d1",
            RawMagneticPointGroup.MPG_312d1p: "MPG_32d1p",
            RawMagneticPointGroup.MPG_321d1p: "MPG_32d1p",
            RawMagneticPointGroup.MPG_312p: "MPG_32p",
            RawMagneticPointGroup.MPG_32p1: "MPG_32p",
            # 3m1 & 31m -> 3m
            RawMagneticPointGroup.MPG_3m1d1: "MPG_3md1",
            RawMagneticPointGroup.MPG_31md1: "MPG_3md1",
            RawMagneticPointGroup.MPG_3m1d1p: "MPG_3md1p",
            RawMagneticPointGroup.MPG_31md1p: "MPG_3md1p",
            RawMagneticPointGroup.MPG_3mp1: "MPG_3mp",
            RawMagneticPointGroup.MPG_31mp: "MPG_3mp",
            # -31m & -3m1 -> -3m
            RawMagneticPointGroup.MPG_b31md1: "MPG_b3md1",
            RawMagneticPointGroup.MPG_b3m1d1: "MPG_b3md1",
            RawMagneticPointGroup.MPG_b31md1p: "MPG_b3md1p",
            RawMagneticPointGroup.MPG_b3m1d1p: "MPG_b3md1p",
            RawMagneticPointGroup.MPG_b3p1m: "MPG_b3pm",      # -3'1m -> -3'm
            RawMagneticPointGroup.MPG_b3pm1: "MPG_b3pm",      # -3'm1 -> -3'm
            RawMagneticPointGroup.MPG_b3p1mp: "MPG_b3pmp",    # -3'1m' -> -3'm'
            RawMagneticPointGroup.MPG_b3pmp1: "MPG_b3pmp",    # -3'm'1 -> -3'm'
            RawMagneticPointGroup.MPG_b31mp: "MPG_b3mp",      # -31m' -> -3m'
            RawMagneticPointGroup.MPG_b3mp1: "MPG_b3mp",      # -3m'1 -> -3m'
            # 622
            RawMagneticPointGroup.MPG_6p2p2: "MPG_6p22p",     # 6'2'2 -> 6'22'
            # 6mm
            RawMagneticPointGroup.MPG_6pmmp: "MPG_6pmpm",     # 6'mm' -> 6'm'm
            # -62m -> -6m2
            RawMagneticPointGroup.MPG_b62md1: "MPG_b6m2d1",   # -62m.1 -> -6m2.1
            RawMagneticPointGroup.MPG_b62md1p: "MPG_b6m2d1p", # -62m.1' -> -6m2.1'
            RawMagneticPointGroup.MPG_b6p2pm: "MPG_b6pm2p",   # -6'2'm -> -6'm2'
            RawMagneticPointGroup.MPG_b6p2mp: "MPG_b6pmp2",   # -6'2m' -> -6'm'2
            RawMagneticPointGroup.MPG_b62pmp: "MPG_b6mp2p",   # -62'm' -> -6m'2'
            # 6/mmm
            RawMagneticPointGroup.MPG_6psmmpm: "MPG_6psmmmp", # 6'/mm'm -> 6'/mmm'
            RawMagneticPointGroup.MPG_6psmpmmp: "MPG_6psmpmpm", # 6'/m'mm' -> 6'/m'm'm
        }

        # 1. まず名前がそのまま一致するか探す
        try:
            return cls[raw.name]
        except KeyError:
            # 2. 一致しなければマッピング辞書で変換して探す
            if raw in RAW_TO_MPG_MAP:
                return cls[RAW_TO_MPG_MAP[raw]]
            
            raise ValueError(f"等価な MagneticPointGroup へのマッピングが見つかりません: {raw}")
        
    @classmethod
    def from_rawstr(cls, s: str) -> 'MagneticPointGroup':
        """
        元の文字列（例: "m-3m.1'" など）から対応するEnumメンバーを取得する
        """
        raw_magnetic_point_group = RawMagneticPointGroup.from_str(s)
        
        return cls.from_raw(raw_magnetic_point_group)

    def is_piezomagnetic_allowed(self) -> bool:
        """
        Piezomagnetic effect（ピエゾ磁気効果）が許容される磁気点群かどうかを返す。
        （時間反転対称性単独1'を持つ群など、許容されない場合は False）
        参照：Piezomagnetic matrices for the 90 magnetic point groups の画像リスト
        """
        # 1. (1, -1)
        if self in {
            MagneticPointGroup.MPG_1d1,
            MagneticPointGroup.MPG_b1d1,
        }:
            return True

        # 2. (2, m, 2/m)
        if self in {
            MagneticPointGroup.MPG_2d1,
            MagneticPointGroup.MPG_md1,
            MagneticPointGroup.MPG_2smd1,
        }:
            return True

        # 3. (2', m', 2'/m')
        if self in {
            MagneticPointGroup.MPG_2p,
            MagneticPointGroup.MPG_mp,
            MagneticPointGroup.MPG_2psmp,
        }:
            return True

        # 4. (222, mm2, mmm)
        if self in {
            MagneticPointGroup.MPG_222d1,
            MagneticPointGroup.MPG_mm2d1,
            MagneticPointGroup.MPG_mmmd1,
        }:
            return True

        # 5. (2'2'2, m'm'2, m'2'm, m'm'm)
        if self in {
            MagneticPointGroup.MPG_2p2p2,
            MagneticPointGroup.MPG_mpmp2,
            MagneticPointGroup.MPG_mpm2p,
            MagneticPointGroup.MPG_mpmpm,
        }:
            return True

        # 6. (3, -3)
        if self in {
            MagneticPointGroup.MPG_3d1,
            MagneticPointGroup.MPG_b3d1,
        }:
            return True

        # 7. (32, 3m, -3m)
        if self in {
            MagneticPointGroup.MPG_32d1,
            MagneticPointGroup.MPG_3md1,
            MagneticPointGroup.MPG_b3md1,
        }:
            return True

        # 8. (32', 3m', -3m')
        if self in {
            MagneticPointGroup.MPG_32p,
            MagneticPointGroup.MPG_3mp,
            MagneticPointGroup.MPG_b3mp,
        }:
            return True

        # 9. (4, -4, 4/m, 6, -6, 6/m)
        if self in {
            MagneticPointGroup.MPG_4d1,
            MagneticPointGroup.MPG_b4d1,
            MagneticPointGroup.MPG_4smd1,
            MagneticPointGroup.MPG_6d1,
            MagneticPointGroup.MPG_b6d1,
            MagneticPointGroup.MPG_6smd1,
        }:
            return True

        # 10. (4', -4', 4'/m)
        if self in {
            MagneticPointGroup.MPG_4p,
            MagneticPointGroup.MPG_b4p,
            MagneticPointGroup.MPG_4psm,
        }:
            return True

        # 11. (422, 4mm, -42m, 4/mmm, 622, 6mm, -6m2, 6/mmm)
        if self in {
            MagneticPointGroup.MPG_422d1,
            MagneticPointGroup.MPG_4mmd1,
            MagneticPointGroup.MPG_b42md1,
            MagneticPointGroup.MPG_4smmmd1,
            MagneticPointGroup.MPG_622d1,
            MagneticPointGroup.MPG_6mmd1,
            MagneticPointGroup.MPG_b6m2d1,
            MagneticPointGroup.MPG_6smmmd1,
        }:
            return True

        # 12. (4'22, 4'mm', -4'2m', -4'2'm, 4'/mmm')
        if self in {
            MagneticPointGroup.MPG_4p22p,   # 4'22'
            MagneticPointGroup.MPG_4pmpm,   # 4'm'm (画像は 4'mm')
            MagneticPointGroup.MPG_b4p2mp,  # -4'2m'
            MagneticPointGroup.MPG_b4p2pm,  # -4'2'm
            MagneticPointGroup.MPG_4psmmpm, # 4'/mmm'
        }:
            return True

        # 13. (42'2', 4m'm', -42'm', 4/mm'm', 62'2', 6m'm', -6m'2', 6/mm'm')
        if self in {
            MagneticPointGroup.MPG_42p2p,   # 42'2'
            MagneticPointGroup.MPG_4mpmp,   # 4m'm'
            MagneticPointGroup.MPG_b42pmp,  # -42'm'
            MagneticPointGroup.MPG_4smmpmp, # 4/mm'm'
            MagneticPointGroup.MPG_62p2p,   # 62'2'
            MagneticPointGroup.MPG_6mpmp,   # 6m'm'
            MagneticPointGroup.MPG_b6mp2p,  # -6m'2'
            MagneticPointGroup.MPG_6smmpmp, # 6/mm'm'
        }:
            return True

        # 14. (6', -6', 6'/m')
        if self in {
            MagneticPointGroup.MPG_6p,
            MagneticPointGroup.MPG_b6p,
            MagneticPointGroup.MPG_6psmp,
        }:
            return True

        # 15. (6'22', 6'mm', -6'm'2, -6'm2', 6'/m'mm')
        if self in {
            MagneticPointGroup.MPG_6p22p,    # 6'22'
            MagneticPointGroup.MPG_6pmpm,    # 6'm'm (画像は 6'mm')
            MagneticPointGroup.MPG_b6pmp2,   # -6'm'2
            MagneticPointGroup.MPG_b6pm2p,   # -6'm2'
            MagneticPointGroup.MPG_6psmpmpm, # 6'/m'mm'
        }:
            return True

        # 16. (23, m-3, 4'32', -4'3m', m-3m')
        if self in {
            MagneticPointGroup.MPG_23d1,    # 23
            MagneticPointGroup.MPG_mb3d1,   # m-3 
            MagneticPointGroup.MPG_4p32p,   # 4'32'
            MagneticPointGroup.MPG_b4p3mp,  # -4'3m'
            MagneticPointGroup.MPG_mb3mp,   # m-3m'
        }:
            return True

        # All other magnetic groups (時間反転対称性を持つものや、上記以外の対称性の高い立方晶系など)
        return False
    
    def is_ferromagnetic_allowed(self) -> bool:
        """
        強磁性秩序（自発磁化）が許容される磁気点群かどうかを返す。
        許容されるのは以下の31個の磁気点群のみ。
        """
        # 三斜晶系 (2個)
        if self in {
            MagneticPointGroup.MPG_1d1,
            MagneticPointGroup.MPG_b1d1,
        }:
            return True

        # 単斜晶系 (6個)
        if self in {
            MagneticPointGroup.MPG_2d1,
            MagneticPointGroup.MPG_md1,
            MagneticPointGroup.MPG_2smd1,
            MagneticPointGroup.MPG_2p,
            MagneticPointGroup.MPG_mp,
            MagneticPointGroup.MPG_2psmp,
        }:
            return True

        # 直方晶系 (4個)
        if self in {
            MagneticPointGroup.MPG_2p2p2,
            MagneticPointGroup.MPG_mpmp2, # m'm'2
            MagneticPointGroup.MPG_mpm2p, # m'm2'
            MagneticPointGroup.MPG_mpmpm, # m'm'm
        }:
            return True

        # 正方晶系 (7個)
        if self in {
            MagneticPointGroup.MPG_4d1,
            MagneticPointGroup.MPG_b4d1,  # -4.1
            MagneticPointGroup.MPG_4smd1, # 4/m.1
            MagneticPointGroup.MPG_42p2p, # 42'2'
            MagneticPointGroup.MPG_4mpmp, # 4m'm'
            MagneticPointGroup.MPG_b42pmp, # -42'm'
            MagneticPointGroup.MPG_4smmpmp, # 4/mm'm'
        }:
            return True

        # 三方晶系 (5個)
        if self in {
            MagneticPointGroup.MPG_3d1,
            MagneticPointGroup.MPG_b3d1,  # -3.1
            MagneticPointGroup.MPG_32p,   # 32'
            MagneticPointGroup.MPG_3mp,   # 3m'
            MagneticPointGroup.MPG_b3mp,  # -3m'
        }:
            return True

        # 六方晶系 (7個)
        if self in {
            MagneticPointGroup.MPG_6d1,
            MagneticPointGroup.MPG_b6d1,  # -6.1
            MagneticPointGroup.MPG_6smd1, # 6/m.1
            MagneticPointGroup.MPG_62p2p, # 62'2'
            MagneticPointGroup.MPG_6mpmp, # 6m'm'
            MagneticPointGroup.MPG_b6mp2p, # -6m'2'
            MagneticPointGroup.MPG_6smmpmp, # 6/mm'm'
        }:
            return True

        return False

# ==========================================
# 実行テスト
# ==========================================
if __name__ == "__main__":
    print(f"厳密な磁気点群の数: {len(MagneticPointGroup)}個 (期待値: 122個)")
    
    # from_str <-> debug_name の可逆性テスト
    assert MagneticPointGroup.from_str("-4'2m'").debug_name() == "-4'2m'"
    
    # 冗長な Raw から厳密な MPG への変換テスト
    raw_sample_1 = RawMagneticPointGroup.MPG_mmp2p # mm'2'
    mapped_1 = MagneticPointGroup.from_raw(raw_sample_1)
    print(f"{raw_sample_1.name} は等価な {mapped_1.debug_name()} にマッピングされました")
    
    # すべての RawMagneticPointGroup がエラーなく変換できるかテスト
    for raw_mpg in RawMagneticPointGroup:
        mapped_mpg = MagneticPointGroup.from_raw(raw_mpg)
        
    print("すべての RawMagneticPointGroup のマッピングテストに合格しました！")