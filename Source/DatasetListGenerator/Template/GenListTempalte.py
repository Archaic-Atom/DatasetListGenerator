# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import os


class GenListTempalte(object):
    __metaclass__ = ABCMeta

    def __init__(self, dataset_folder_path: str, save_folder_path: str) -> None:
        super().__init__()
        self._dataset_folder_path = dataset_folder_path
        self._save_folder_path = save_folder_path

    @property
    def dataset_folder_path(self) -> str:
        return self._dataset_folder_path

    @property
    def save_folder_path(self) -> str:
        return self._save_folder_path

    @abstractmethod
    def exec(self) -> None:
        pass

    def open_file(self, path: str) -> object:
        if os.path.exists(path):
            os.remove(path)
        return open(path, 'a')

    def write_file(self, fd_file: object, data_str: str) -> None:
        fd_file.write(data_str + '\n')
        fd_file.flush()

    def close_file(self, fd_file: object) -> None:
        fd_file.close()

    def get_folders_path(self, path: str) -> list:
        folders, offset = [], 1
        files = os.listdir(path)
        for file in files:
            folder_path = os.path.join(path, file)
            if os.path.isdir(folder_path):
                pos = folder_path.rfind('/') + offset
                folders.append(folder_path[pos:])
        return folders
