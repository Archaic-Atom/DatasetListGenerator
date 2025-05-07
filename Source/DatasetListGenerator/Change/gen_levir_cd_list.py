# -*- coding: utf-8 -*-
import os
import glob
from ._meta_change_detection_ops import MetaChangeDetectionOps


class LevirCDList(MetaChangeDetectionOps):
    """docstring for ClassName"""
    ID_PRE_IMG, ID_POST_IMG, ID_GT_IMG = 0, 1, 2

    def __init__(self, dataset_folder_path: str, save_folder_path: str):
        super().__init__(dataset_folder_path, save_folder_path)
        self._training_list = 'levir_cd_training_list.csv'
        self._testing_list = 'levir_cd_testing_list.csv'

    @staticmethod
    def _get_file_path(root_path: str, sub_folder_list: list, file_name: str) -> tuple:
        t1_img_path = os.path.join(root_path, sub_folder_list[LevirCDList.ID_PRE_IMG], file_name)
        t2_img_path = os.path.join(root_path, sub_folder_list[LevirCDList.ID_POST_IMG], file_name)
        gt_path = os.path.join(root_path, sub_folder_list[LevirCDList.ID_GT_IMG], file_name)
        return t1_img_path, t2_img_path, gt_path

    def _gen_list(self, save_file_name: str, sub_folder: str) -> int:
        file_num, off_set = 0, 1
        fd_file = self._open_file(os.path.join(self.save_folder_path, save_file_name))
        sub_folder_list = ['A', 'B', 'label']
        root_path = os.path.join(self.dataset_folder_path, sub_folder)
        t1_img_folder_path = os.path.join(root_path, sub_folder_list[self.ID_PRE_IMG])
        files = glob.glob(os.path.join(t1_img_folder_path, '*.png'))
        for t1_img_path in files:
            filename = os.path.basename(t1_img_path)
            t1_img_path, t2_img_path, gt_path = self._get_file_path(root_path,
                                                                    sub_folder_list,
                                                                    filename)
            if not self._check_file_path(t1_img_path, t2_img_path, gt_path):
                print(f'{t1_img_path} is not exists')
                break

            self.write_file(fd_file, f'{t1_img_path},{t2_img_path},{gt_path}')
            file_num += off_set

        self.close_file(fd_file)
        print('the training file num:', file_num)
        return file_num

    def _gen_training_list(self) -> int:
        return self._gen_list(self._training_list, 'train')

    def _gen_testing_list(self) -> int:
        return self._gen_list(self._testing_list, 'test')

    def exec(self) -> None:
        self._gen_training_list()
        self._gen_testing_list()
