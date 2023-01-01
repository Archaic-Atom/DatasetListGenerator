# -*- coding: utf-8 -*-
import os
from ._meta_stereo_ops import MetaStereoOps


class GenInstereo2KList(MetaStereoOps):
    def __init__(self, dataset_folder_path: str, save_folder_path: str) -> None:
        super().__init__(dataset_folder_path, save_folder_path)
        self._save_training_list_path = os.path.join(
            save_folder_path, 'instereo2K_training_list.csv')
        self._save_testing_list_path = os.path.join(
            save_folder_path, 'instereo2K_testing_list.csv')

    @staticmethod
    def _get_file_path(folder_path: str, img_folder: str) -> tuple:
        left_img_path = os.path.join(folder_path, img_folder, 'left.png')
        right_img_path = os.path.join(folder_path, img_folder, 'right.png')
        disp_path = os.path.join(folder_path, img_folder, 'left_disp.png')
        return left_img_path, right_img_path, disp_path

    def _gen_list(self, save_path: str, sub_folder_list: list, is_training: bool) -> int:
        file_num, off_set = 0, 1
        fd_file = self._open_file(save_path)

        for sub_folder in sub_folder_list:
            folder_path = os.path.join(self.dataset_folder_path, sub_folder)
            img_folder_list = os.listdir(folder_path)
            for img_folder in img_folder_list:
                left_img_path, right_img_path, disp_path = self._get_file_path(
                    folder_path, img_folder)

                if not self._check_file_path(
                        left_img_path, right_img_path, disp_path, is_training):
                    break

                self.write_file(
                    fd_file, left_img_path + ',' + right_img_path + ',' + disp_path)
                file_num = file_num + off_set
        self.close_file(fd_file)
        return file_num

    def _gen_training_list(self) -> int:
        sub_folder_list = ['train/part1', 'train/part2', 'train/part3',
                           'train/part5', 'train/part4', 'train/part6']
        return self._gen_list(self._save_training_list_path, sub_folder_list, True)

    def _gen_testing_list(self) -> int:
        sub_folder_list = ['test/test']
        return self._gen_list(self._save_testing_list_path, sub_folder_list, False)

    def exec(self) -> None:
        file_num = self._gen_training_list()
        print('the training file num:', file_num)
        file_num = self._gen_testing_list()
        print('the testing file num:', file_num)
