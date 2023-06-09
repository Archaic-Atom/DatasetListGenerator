# -*- coding: utf-8 -*-
import os
import glob
from ._meta_stereo_ops import MetaStereoOps


class WHUStereoList(MetaStereoOps):
    TEST_FOLDER = 'test'
    TRAIN_FOLDER = 'train'
    VAL_FOLDER = 'val'

    def __init__(self, dataset_folder_path: str, save_folder_path: str) -> None:
        super().__init__(dataset_folder_path, save_folder_path)
        self._training_list = 'whu_stereo_training_list.csv'
        self._val_list = 'whu_stereo_val_list.csv'
        self._testing_list = 'whu_stereo_testing_list.csv'

    @staticmethod
    def _get_file_folder(root_path: str) -> tuple:
        return root_path + '/left/', root_path + '/right/', root_path + '/disp/'

    def _gen_list(self, root_path: str, save_path: object) -> None:
        file_num, off_set = 0, 1
        fd_file = self._open_file(save_path)

        left_img_folder, right_img_folder, disp_folder = self._get_file_folder(root_path)
        left_files = glob.glob(os.path.join(left_img_folder, '*.tiff'))

        for left_file_name in left_files:
            left_file_name = os.path.basename(left_file_name)
            left_file_path = os.path.join(left_img_folder, left_file_name)
            right_file_path = os.path.join(right_img_folder,
                                           left_file_name.replace('left', 'right'))
            disp_file_path = os.path.join(disp_folder, left_file_name.replace('left', 'disparity'))

            if self._check_file_path(left_file_path, right_file_path, disp_file_path):
                self.write_file(fd_file,
                                left_file_path + ',' + right_file_path + ',' + disp_file_path)
            file_num = file_num + off_set
        self.close_file(fd_file)
        print('total file: ', file_num)

    def _gen_training_list(self) -> None:
        self._gen_list(os.path.join(self.dataset_folder_path, self.TRAIN_FOLDER),
                       os.path.join(self._save_folder_path, self._training_list))

    def _gen_val_list(self) -> None:
        self._gen_list(os.path.join(self.dataset_folder_path, self.VAL_FOLDER),
                       os.path.join(self._save_folder_path, self._val_list))

    def _gen_testing_list(self) -> None:
        self._gen_list(os.path.join(self.dataset_folder_path, self.TEST_FOLDER),
                       os.path.join(self._save_folder_path, self._testing_list))

    def exec(self) -> None:
        self._gen_training_list()
        self._gen_val_list()
        self._gen_testing_list()
