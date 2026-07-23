from enum import Enum, auto


class ConductivityComponent(Enum):
    NLD = auto()
    BCD = auto()
    INTER_QMD = auto()
    INTRA_QMD = auto()
    EXAMPLE = auto()

    def debug_name(self):
        if self == ConductivityComponent.NLD:
            return "NLD"
        elif self == ConductivityComponent.BCD:
            return "BCD"
        elif self == ConductivityComponent.INTER_QMD:
            return "INTER_QMD"
        elif self == ConductivityComponent.INTRA_QMD:
            return "INTRA_QMD"
        elif self == ConductivityComponent.EXAMPLE:
            return "Ex."
        else:
            return "Unknown"
