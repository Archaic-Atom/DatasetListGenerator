# -*- coding: utf-8 -*-
import os
import glob
from ._meta_stereo_ops import MetaStereoOps


class KITTI2015StereoList(MetaStereoOps):
    TRAINING_DATA_FOLDER = 'training/%s'
    TESTING_DATA_FOLDER = 'testing/%s'
    LEFT_FOLDER = 'image_2'
    RIGHT_FOLDER = 'image_3'
    LABLE_FOLDER = 'disp_occ_0'
    FILE_NAME = '%06d_10.png'
    TESTING_IMG_NUM = 200
    TRAINING_IMG_NUM = 200

    def __init__(self, dataset_folder_path: str, save_folder_path: str) -> None:
        super().__init__(dataset_folder_path, save_folder_path)
        self._training_list = 'kitti2015_stereo_training_list.csv'
        self._testing_list = 'kitti2015_stereo_testing_list.csv'

    def _gen_path(self, file_folder: str, num: int) -> None:
        path = os.path.join(self.dataset_folder_path, file_folder, self.FILE_NAME % num)
        return path

    def _gen_training_list(self) -> None:
        file_num, off_set = 0, 1
        fd_file = self._open_file(os.path.join(self.save_folder_path, self._training_list))
        for i in range(self.TRAINING_IMG_NUM):
            left_img_path = self._gen_path(self.TRAINING_DATA_FOLDER % self.LEFT_FOLDER, i)
            right_img_path = self._gen_path(self.TRAINING_DATA_FOLDER % self.RIGHT_FOLDER, i)
            disp_path = self._gen_path(self.TRAINING_DATA_FOLDER % self.LABLE_FOLDER, i)
            if self._check_file_path(left_img_path, right_img_path, disp_path):
                self.write_file(fd_file, f'{left_img_path},{right_img_path},{disp_path}')
            else:
                break

            file_num = file_num + off_set
        self.close_file(fd_file)
        print('total file: ', file_num)

    def _gen_testing_list(self) -> None:
        file_num, off_set = 0, 1
        fd_file = self._open_file(os.path.join(self.save_folder_path, self._testing_list))

        disp_path = 'None'

        for i in range(self.TRAINING_IMG_NUM):
            left_img_path = self._gen_path(self.TESTING_DATA_FOLDER % self.LEFT_FOLDER, i)
            right_img_path = self._gen_path(self.TESTING_DATA_FOLDER % self.RIGHT_FOLDER, i)
            if self._check_file_path(left_img_path, right_img_path, disp_path, is_training=False):
                self.write_file(fd_file, f'{left_img_path},{right_img_path},{disp_path}')
            else:
                break

            file_num = file_num + off_set
        self.close_file(fd_file)
        print('total file: ', file_num)

    def exec(self) -> None:
        self._gen_training_list()
        self._gen_testing_list()
