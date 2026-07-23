from core.conductivity_component import ConductivityComponent
from core.nlh_tensor import nlh

from dataclasses import dataclass
from typing import Self

@dataclass
class tensor_character:
    uni_number : int
    has_NLD : bool
    has_BCD : bool
    has_interQMD : bool
    has_intraQMD : bool
    has_NLD_after_2_index_is_same : bool
    has_BCD_after_2_index_is_same : bool
    has_interQMD_after_2_index_is_same : bool
    has_intraQMD_after_2_index_is_same : bool
    transverse_NLD : tuple[bool, bool, bool]
    transverse_intraQMD : tuple[bool, bool, bool]
    has_transverse_NLD : bool
    has_transverse_intraQMD : bool

    @classmethod
    def new(cls,uni_number : int) -> Self:
        tensor_NLD = nlh.read(uni_number, ConductivityComponent.NLD)
        tensor_BCD = nlh.read(uni_number, ConductivityComponent.BCD)
        tensor_interQMD = nlh.read(uni_number, ConductivityComponent.INTER_QMD)
        tensor_intraQMD = nlh.read(uni_number, ConductivityComponent.INTRA_QMD)

        transverse_NLD = tensor_NLD.allow_transvese_component()
        transverse_intraQMD = tensor_intraQMD.allow_transvese_component()

        if transverse_NLD == (False, False, False):
            has_transverse_NLD = False
        else:
            has_transverse_NLD = True

        if transverse_intraQMD == (False, False, False):
            has_transverse_intraQMD = False
        else:
            has_transverse_intraQMD = True

        return cls(
            uni_number=uni_number,
            has_NLD=tensor_NLD.is_nonzero(),
            has_BCD=tensor_BCD.is_nonzero(),
            has_interQMD=tensor_interQMD.is_nonzero(),
            has_intraQMD=tensor_intraQMD.is_nonzero(),
            has_NLD_after_2_index_is_same=tensor_NLD.contain_after_2_index_is_same(),
            has_BCD_after_2_index_is_same=tensor_BCD.contain_after_2_index_is_same(),
            has_interQMD_after_2_index_is_same=tensor_interQMD.contain_after_2_index_is_same(),
            has_intraQMD_after_2_index_is_same=tensor_intraQMD.contain_after_2_index_is_same(),
            transverse_NLD=transverse_NLD,
            transverse_intraQMD=transverse_intraQMD,
            has_transverse_NLD=has_transverse_NLD,
            has_transverse_intraQMD=has_transverse_intraQMD
        )  
    
    def transverse_QMD_component(self) -> str:
        transerse_intraQMD = self.transverse_intraQMD

        list = []

        if transerse_intraQMD[0] is True:
            list.append("x")
        if transerse_intraQMD[1] is True:
            list.append("y")
        if transerse_intraQMD[2] is True:
            list.append("z")   

        return ", ".join(list)
