# -*- coding: utf-8 -*-
from .gen_whu_stereo_list import WHUStereoList
from .gen_cre_stereo_list import CreStereoList


def _get_generator_dict() -> dict:
    return {'WHUStereo': WHUStereoList, 'CREStereo': CreStereoList}


def stereo_dataset_selection(dataset: str) -> None:
    dataset_cls_dict = _get_generator_dict()
    return dataset_cls_dict[dataset]
