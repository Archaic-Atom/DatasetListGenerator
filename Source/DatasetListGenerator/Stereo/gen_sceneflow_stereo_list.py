# -*- coding: utf-8 -*-
import os
import glob
from ._meta_stereo_ops import MetaStereoOps


class SceneFlowStereoList(MetaStereoOps):
    DRIVING_LIST = ['15mm_focallength/scene_backwards/fast',
                    '15mm_focallength/scene_backwards/slow',
                    '15mm_focallength/scene_forwards/fast',
                    '15mm_focallength/scene_forwards/slow',
                    '35mm_focallength/scene_backwards/fast',
                    '35mm_focallength/scene_backwards/slow',
                    '35mm_focallength/scene_forwards/fast',
                    '35mm_focallength/scene_forwards/slow']
    MONKEY_LIST = ['a_rain_of_stones_x2', 'eating_camera2_x2',
                   'eating_naked_camera2_x2', 'eating_x2',
                   'family_x2', 'flower_storm_augmented0_x2',
                   'flower_storm_augmented1_x2', 'flower_storm_x2',
                   'funnyworld_augmented0_x2', 'funnyworld_augmented1_x2',
                   'funnyworld_camera2_augmented0_x2', 'funnyworld_camera2_augmented1_x2',
                   'funnyworld_camera2_x2', 'funnyworld_x2',
                   'lonetree_augmented0_x2', 'lonetree_augmented1_x2',
                   'lonetree_difftex2_x2', 'lonetree_difftex_x2',
                   'lonetree_winter_x2', 'lonetree_x2', 'top_view_x2',
                   'treeflight_augmented0_x2', 'treeflight_augmented1_x2',
                   'treeflight_x2']
    FLYING_LIST = ['A', 'B', 'C']

    def __init__(self, dataset_folder_path: str, save_folder_path: str) -> None:
        super().__init__(dataset_folder_path, save_folder_path)
        self._training_list = 'sceneflow_stereo_training_list.csv'
        self._testing_list = 'sceneflow_stereo_testing_list.csv'

    def _produce_list(self, folder_list: list, img_root_path: str,
                      disp_root_path: str, fd_file: object) -> int:
        file_num, off_set = 0, 1

        for folder in folder_list:
            for left_file in glob.glob(
                    os.path.join(img_root_path, folder, 'left', '*')):
                name = self._get_file_name(left_file)
                left_img_path = os.path.join(
                    img_root_path, folder, 'left', f'{name}.png')
                right_img_path = os.path.join(
                    img_root_path, folder, 'right', f'{name}.png')
                disp_path = os.path.join(
                    disp_root_path, folder, 'left', f'{name}.pfm')
                if self._check_file_path(left_img_path, right_img_path, disp_path, True):
                    self.write_file(fd_file, f'{left_img_path},{right_img_path},{disp_path}')
                    file_num = file_num + off_set
        return file_num

    @staticmethod
    def _get_file_name(path: str) -> str:
        name = os.path.basename(path)
        pos = name.find('.png')
        return name[:pos]

    def _gen_list_flyingthing(
            self, img_root_path: str, disp_root_path: str, fd_file: object) -> int:
        file_num, off_set = 0, 1
        for folder in self.FLYING_LIST:
            for sub_folder in self.get_folders_path(os.path.join(img_root_path, folder)):
                for left_img in glob.glob(
                        os.path.join(img_root_path, folder, sub_folder, 'left', '*')):
                    name = self._get_file_name(left_img)
                    left_img_path = os.path.join(
                        img_root_path, folder, sub_folder, 'left', f'{name}.png')
                    right_img_path = os.path.join(
                        img_root_path, folder, sub_folder, 'right', f'{name}.png')
                    disp_path = os.path.join(
                        disp_root_path, folder, sub_folder, 'left', f'{name}.pfm')

                    if self._check_file_path(left_img_path, right_img_path, disp_path, True):
                        self.write_file(fd_file, f'{left_img_path},{right_img_path},{disp_path}')
                        file_num = file_num + off_set
        return file_num

    def _gen_list_driving(self, img_root_path: str, disp_root_path: str, fd_file: object) -> int:
        return self._produce_list(self.DRIVING_LIST, img_root_path, disp_root_path, fd_file)

    def _gen_list_monkey(self, img_root_path: str, disp_root_path: str, fd_file: object) -> int:
        return self._produce_list(self.MONKEY_LIST, img_root_path, disp_root_path, fd_file)

    def _gen_root_path(self, is_training: bool) -> tuple:
        save_list_path = self._training_list if is_training else self._testing_list
        fd_file = self._open_file(os.path.join(self._save_folder_path, save_list_path))
        img_root_path = os.path.join(
            self._dataset_folder_path,
            'frames_finalpass/TRAIN' if is_training else 'frames_finalpass/TEST')
        disp_root_path = os.path.join(
            self._dataset_folder_path,
            'disparity/TRAIN' if is_training else 'disparity/TEST')
        return fd_file, img_root_path, disp_root_path

    def _gen_training_list(self) -> None:
        fd_file, img_root_path, disp_root_path = self._gen_root_path(True)
        flying_num = self._gen_list_flyingthing(img_root_path, disp_root_path, fd_file)
        driving_num = self._gen_list_driving(img_root_path, disp_root_path, fd_file)
        monkey_num = self._gen_list_monkey(img_root_path, disp_root_path, fd_file)
        self.close_file(fd_file)
        print('total (training): ', flying_num + driving_num + monkey_num)

    def _gen_testing_list(self) -> None:
        fd_file, img_root_path, disp_root_path = self._gen_root_path(False)
        flying_num = self._gen_list_flyingthing(img_root_path, disp_root_path, fd_file)
        self.close_file(fd_file)
        print('total (testing): ', flying_num)

    def exec(self) -> None:
        self._gen_training_list()
        self._gen_testing_list()
