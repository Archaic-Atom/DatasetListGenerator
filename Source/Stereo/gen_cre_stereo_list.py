# -*- coding: utf-8 -*-
import os
import glob
from ._meta_stereo_ops import MetaStereoOps


class CreStereoList(MetaStereoOps):
    """docstring for ClassName"""
    LEFT_IMG_NAME = '_left.jpg'
    RIGHT_IMG_NAME = '_right.jpg'
    DISP_NAME = '_left.disp.png'

    def __init__(self, dataset_folder_path: str, save_folder_path: str):
        super().__init__(dataset_folder_path, save_folder_path)
        self._training_list = 'cretereo_training_list.csv'

    def _open_file(self, file_path: str) -> object:
        fd_file = self.open_file(file_path)
        self.write_file(fd_file, 'left_img,right_img,gt_disp')
        return fd_file

    @staticmethod
    def _get_file_path(root_path: str, file_name: str) -> tuple:
        left_img_path = os.path.join(root_path, file_name + CreStereoList.LEFT_IMG_NAME)
        right_img_path = os.path.join(root_path, file_name + CreStereoList.RIGHT_IMG_NAME)
        disp_path = os.path.join(root_path, file_name + CreStereoList.DISP_NAME)
        return left_img_path, right_img_path, disp_path

    def _gen_training_list(self) -> int:
        file_num, off_set = 0, 1
        fd_file = self._open_file(os.path.join(self.save_folder_path, self._training_list))
        sub_folder_list = ['hole', 'reflective', 'shapenet', 'tree']

        for folder_name in sub_folder_list:
            root_path = os.path.join(self.dataset_folder_path, folder_name)
            files = glob.glob(os.path.join(root_path, '*_left.jpg'))
            for left_file_name in files:
                file_name = left_file_name[:-len(CreStereoList.LEFT_IMG_NAME)]
                left_img_path, right_img_path, disp_path = self._get_file_path(root_path, file_name)

                if not self._check_file_path(
                        left_img_path, right_img_path, disp_path):
                    print(left_img_path + ' is not exists')
                    break

                self.write_file(
                    fd_file, left_img_path + ',' + right_img_path + ',' + disp_path)
                file_num = file_num + off_set
        self.close_file(fd_file)
        return file_num

    def exec(self) -> None:
        file_num = self._gen_training_list()
        print('the training file num:', file_num)
