# -*- coding: utf-8 -*-
from .gen_whu_reconstruction_list import WHUReconstructionList
from .gen_us3d_reconstruction_list import US3DReconstructionList


def _get_generator_dict() -> dict:
    return {'WHUReconstruction': WHUReconstructionList,
            'US3DReconstruction': US3DReconstructionList}


def reconstruction_dataset_selection(dataset: str) -> None:
    dataset_cls_dict = _get_generator_dict()
    return dataset_cls_dict[dataset]
