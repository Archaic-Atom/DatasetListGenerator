# -*- coding: utf-8 -*-
import os
from DatasetListGenerator.Template import GenListTempalte


class MetaStereoOps(GenListTempalte):
    """docstring for ClassName"""

    def __init__(self, dataset_folder_path: str, save_folder_path: str) -> None:
        super().__init__(dataset_folder_path, save_folder_path)

    @staticmethod
    def _check_file_path(left_img_path: str, right_img_path: str,
                         disp_path: str, is_training: bool = True) -> bool:
        res = True
        if (not os.path.exists(left_img_path)) and (not os.path.exists(right_img_path)):
            res = False
        if is_training and (not os.path.exists(disp_path)):
            res = False
        return res

    def _open_file(self, file_path: str) -> object:
        fd_file = self.open_file(file_path)
        self.write_file(fd_file, 'left_img,right_img,gt_disp')
        return fd_file
