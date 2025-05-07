# -*- coding: utf-8 -*-
import os
from DatasetListGenerator.Template import GenListTempalte


class MetaChangeDetectionOps(GenListTempalte):
    """docstring for ClassName"""

    def __init__(self, dataset_folder_path: str, save_folder_path: str) -> None:
        super().__init__(dataset_folder_path, save_folder_path)

    @staticmethod
    def _check_file_path(t1_img_path: str, t2_img_path: str,
                         label_path: str, is_training: bool = True) -> bool:
        res = True
        if (not os.path.exists(t1_img_path)) and (not os.path.exists(t2_img_path)):
            res = False
        if is_training and (not os.path.exists(label_path)):
            res = False
        return res

    def _open_file(self, file_path: str) -> object:
        fd_file = self.open_file(file_path)
        self.write_file(fd_file, 'T1,T2,gt')
        return fd_file
