# -*- coding: utf-8 -*-
import os
import glob
import random
from ._meta_reconstruction_ops import MetaStereoOps


class US3DReconstructionList(MetaStereoOps):
    TEST_FOLDER = 'Track_Test'
    TRAIN_FOLDER = 'Track_Train'
    TRACK_FORMAT = ['*LEFT_RGB*.tif', 'LEFT_RGB', 'RIGHT_RGB.tif']
    VAL_NUM = 50

    def __init__(self, dataset_folder_path: str, save_folder_path: str) -> None:
        super().__init__(dataset_folder_path, save_folder_path)
        self._training_list = 'us3d_reconstruction_training_list.csv'
        self._val_list = 'us3d_reconstruction_val_list.csv'
        self._testing_list = 'us3d_reconstruction_testing_list.csv'

    def _write_file(self, path: str, fd_file: object) -> None:
        if self._check_file_path(path):
            self.write_file(fd_file, path)

    def _gen_training_list(self) -> None:
        file_num, off_set = 0, 1
        training_fd_file = self._open_file(os.path.join(self.save_folder_path, self._training_list))
        val_fd_file = self._open_file(os.path.join(self.save_folder_path, self._val_list))
        root_path = os.path.join(self.dataset_folder_path, self.TRAIN_FOLDER)
        files = glob.glob(root_path + '/' + self.TRACK_FORMAT[0])
        val_list = random.sample(range(0, len(files)), self.VAL_NUM)
        for idx, left_file_path in enumerate(files):
            left_name = os.path.basename(left_file_path)
            start = left_name.find(self.TRACK_FORMAT[1])
            right_file_path = os.path.join(root_path, left_name[0:start] + self.TRACK_FORMAT[2])
            fd_file = val_fd_file if idx in val_list else training_fd_file
            self._write_file(left_file_path, fd_file)
            self._write_file(right_file_path, fd_file)

            file_num = file_num + off_set
        self.close_file(training_fd_file)
        self.close_file(val_fd_file)
        print('total training file: ', file_num)

    def _gen_testing_list(self) -> None:
        file_num, off_set = 0, 1
        fd_file = self._open_file(os.path.join(self.save_folder_path, self._testing_list))
        root_path = os.path.join(self.dataset_folder_path, self.TEST_FOLDER)
        files = glob.glob(root_path + '/' + self.TRACK_FORMAT[0])
        for _, left_file_path in enumerate(files):
            left_name = os.path.basename(left_file_path)
            start = left_name.find(self.TRACK_FORMAT[1])
            right_file_path = os.path.join(root_path, left_name[0:start] + self.TRACK_FORMAT[2])
            self._write_file(left_file_path, fd_file)
            self._write_file(right_file_path, fd_file)
            file_num = file_num + off_set
        self.close_file(fd_file)
        print('total testing file: ', file_num)

    def exec(self) -> None:
        self._gen_training_list()
        self._gen_testing_list()
