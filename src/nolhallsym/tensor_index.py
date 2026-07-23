from dataclasses import dataclass

import sympy as sp


SIGMA_VARS = sp.symbols("xxx xxy xxz xyy xyz xzz yxx yxy yxz yyy yyz yzz zxx zxy zxz zyy zyz zzz")


@dataclass
class ABC:
    a: int
    b: int
    c: int

    def index_2_num(self) -> int:
        """
        3次元テンソルのインデックス (a,b,c) を、1次元配列のインデックスに変換する
        a,b,c は 0,1,2 のいずれかであることを想定
        """
        if self.a == 0 and self.b == 0 and self.c == 0:
            return 0
        elif self.a == 0 and ((self.b == 0 and self.c == 1) or (self.b == 1 and self.c == 0)):
            return 1
        elif self.a == 0 and ((self.b == 0 and self.c == 2) or (self.b == 2 and self.c == 0)):
            return 2
        elif self.a == 0 and self.b == 1 and self.c == 1:
            return 3
        elif self.a == 0 and ((self.b == 1 and self.c == 2) or (self.b == 2 and self.c == 1)):
            return 4
        elif self.a == 0 and self.b == 2 and self.c == 2:
            return 5
        elif self.a == 1 and self.b == 0 and self.c == 0:
            return 6
        elif self.a == 1 and ((self.b == 0 and self.c == 1) or (self.b == 1 and self.c == 0)):
            return 7
        elif self.a == 1 and ((self.b == 0 and self.c == 2) or (self.b == 2 and self.c == 0)):
            return 8
        elif self.a == 1 and self.b == 1 and self.c == 1:
            return 9
        elif self.a == 1 and ((self.b == 1 and self.c == 2) or (self.b == 2 and self.c == 1)):
            return 10
        elif self.a == 1 and self.b == 2 and self.c == 2:
            return 11
        elif self.a == 2 and self.b == 0 and self.c == 0:
            return 12
        elif self.a == 2 and ((self.b == 0 and self.c == 1) or (self.b == 1 and self.c == 0)):
            return 13
        elif self.a == 2 and ((self.b == 0 and self.c == 2) or (self.b == 2 and self.c == 0)):
            return 14
        elif self.a == 2 and self.b == 1 and self.c == 1:
            return 15
        elif self.a == 2 and ((self.b == 1 and self.c == 2) or (self.b == 2 and self.c == 1)):
            return 16
        elif self.a == 2 and self.b == 2 and self.c == 2:
            return 17
        else:
            raise ValueError(f"Invalid indices: (a,b,c)=({self.a},{self.b},{self.c})")

    @staticmethod
    def num_2_index(num: int) -> 'ABC':
        """
        1次元配列のインデックスを、3次元テンソルのインデックス (a,b,c) に変換する
        num は 0〜17 の範囲であることを想定
        """
        if num == 0:
            return ABC(0, 0, 0)
        elif num == 1:
            return ABC(0, 0, 1)
        elif num == 2:
            return ABC(0, 0, 2)
        elif num == 3:
            return ABC(0, 1, 1)
        elif num == 4:
            return ABC(0, 1, 2)
        elif num == 5:
            return ABC(0, 2, 2)
        elif num == 6:
            return ABC(1, 0, 0)
        elif num == 7:
            return ABC(1, 0, 1)
        elif num == 8:
            return ABC(1, 0, 2)
        elif num == 9:
            return ABC(1, 1, 1)
        elif num == 10:
            return ABC(1, 1, 2)
        elif num == 11:
            return ABC(1, 2, 2)
        elif num == 12:
            return ABC(2, 0, 0)
        elif num == 13:
            return ABC(2, 0, 1)
        elif num == 14:
            return ABC(2, 0, 2)
        elif num == 15:
            return ABC(2, 1, 1)
        elif num == 16:
            return ABC(2, 1, 2)
        elif num == 17:
            return ABC(2, 2, 2)
        else:
            raise ValueError(f"Invalid number: {num}. Must be in range [0-17].")
