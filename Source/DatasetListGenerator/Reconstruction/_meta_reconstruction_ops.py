# -*- coding: utf-8 -*-
import os
from DatasetListGenerator.Template import GenListTempalte


class MetaStereoOps(GenListTempalte):
    """docstring for ClassName"""

    def __init__(self, dataset_folder_path: str, save_folder_path: str) -> None:
        super().__init__(dataset_folder_path, save_folder_path)

    @staticmethod
    def _check_file_path(img_path: str) -> bool:
        res = True
        if not os.path.exists(img_path):
            res = False
        return res

    def _open_file(self, file_path: str) -> object:
        fd_file = self.open_file(file_path)
        self.write_file(fd_file, 'img')
        return fd_file
