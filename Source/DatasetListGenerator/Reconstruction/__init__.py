# -*- coding: utf-8 -*-
from .gen_whu_reconstruction_list import WHUReconstructionList


def _get_generator_dict() -> dict:
    return {'WHUReconstruction': WHUReconstructionList}


def reconstruction_dataset_selection(dataset: str) -> None:
    dataset_cls_dict = _get_generator_dict()
    return dataset_cls_dict[dataset]
