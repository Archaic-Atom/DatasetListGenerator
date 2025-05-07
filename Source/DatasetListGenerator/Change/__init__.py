# -*- coding: utf-8 -*-
from .gen_levir_cd_list import LevirCDList


def _get_generator_dict() -> dict:
    return {'LEVIR-CD': LevirCDList, }


def change_detection_dataset_selection(dataset: str) -> None:
    dataset_cls_dict = _get_generator_dict()
    return dataset_cls_dict[dataset]
