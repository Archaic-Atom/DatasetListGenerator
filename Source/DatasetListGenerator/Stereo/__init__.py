# -*- coding: utf-8 -*-
from .gen_whu_stereo_list import WHUStereoList
from .gen_cre_stereo_list import CreStereoList
from .gen_kitti2012_stereo_list import KITTI2012StereoList
from .gen_kitti2015_stereo_list import KITTI2015StereoList
from .gen_eth3d_stereo_list import ETH3DStereoList
from .gen_middlebury_stereo_list import MiddleburyStereoList
from .gen_us3d_stereo_list import US3DStereoList
from .gen_sceneflow_stereo_list import SceneFlowStereoList


def _get_generator_dict() -> dict:
    return {'WHUStereo': WHUStereoList, 'CREStereo': CreStereoList,
            'KITTI2012': KITTI2012StereoList, 'KITTI2015': KITTI2015StereoList,
            'ETH3D': ETH3DStereoList, 'Middlebury': MiddleburyStereoList,
            'US3D': US3DStereoList, 'SceneFlow': SceneFlowStereoList}


def stereo_dataset_selection(dataset: str) -> None:
    dataset_cls_dict = _get_generator_dict()
    return dataset_cls_dict[dataset]
