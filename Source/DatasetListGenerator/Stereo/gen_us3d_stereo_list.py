# -*- coding: utf-8 -*-
import os
import glob
import random
from ._meta_stereo_ops import MetaStereoOps


class US3DStereoList(MetaStereoOps):
    TEST_FOLDER = 'Track_Test'
    TRAIN_FOLDER = 'Track_Train'
    TRACK_FORMAT = ['*LEFT_RGB*.tif', 'LEFT_RGB', 'RIGHT_RGB.tif', 'LEFT_DSP.tif']
    VAL_NUM = 50

    def __init__(self, dataset_folder_path: str, save_folder_path: str) -> None:
        super().__init__(dataset_folder_path, save_folder_path)
        self._training_list = 'us3d_stereo_training_list.csv'
        self._val_list = 'us3d_stereo_val_list.csv'
        self._testing_list = 'us3d_stereo_testing_list.csv'

    def _gen_training_list(self) -> None:
        file_num, off_set = 0, 1
        training_fd_file = self._open_file(os.path.join(self.save_folder_path, self._training_list))
        val_fd_file = self._open_file(os.path.join(self.save_folder_path, self._val_list))
        root_path = os.path.join(self.dataset_folder_path, self.TRAIN_FOLDER)
        files = glob.glob(f'{root_path}/{self.TRACK_FORMAT[0]}')
        val_list = random.sample(range(len(files)), self.VAL_NUM)
        for idx, left_file_path in enumerate(files):
            left_name = os.path.basename(left_file_path)
            start = left_name.find(self.TRACK_FORMAT[1])
            right_file_path = os.path.join(
                root_path, left_name[:start] + self.TRACK_FORMAT[2])
            disp_file_path = os.path.join(
                root_path, left_name[:start] + self.TRACK_FORMAT[3])

            if self._check_file_path(left_file_path, right_file_path, disp_file_path):
                if idx in val_list:
                    self.write_file(training_fd_file,
                                    f'{left_file_path},{right_file_path},{disp_file_path}',)
                else:
                    self.write_file(val_fd_file,
                                    f'{left_file_path},{right_file_path},{disp_file_path}',)
            file_num = file_num + off_set
        self.close_file(training_fd_file)
        self.close_file(val_fd_file)
        print('total training file: ', file_num)

    def _gen_testing_list(self) -> None:
        file_num, off_set = 0, 1
        fd_file = self._open_file(os.path.join(self.save_folder_path, self._testing_list))
        root_path = os.path.join(self.dataset_folder_path, self.TEST_FOLDER)
        files = glob.glob(f'{root_path}/{self.TRACK_FORMAT[0]}')
        disp_file_path = 'None'

        for left_file_path in files:
            left_name = os.path.basename(left_file_path)
            start = left_name.find(self.TRACK_FORMAT[1])
            right_file_path = os.path.join(
                root_path, left_name[:start] + self.TRACK_FORMAT[2]
            )
            if self._check_file_path(left_file_path, right_file_path, disp_file_path, False):
                self.write_file(
                    fd_file, f'{left_file_path},{right_file_path},{disp_file_path}'
                )
            file_num = file_num + off_set
        self.close_file(fd_file)
        print('total testing file: ', file_num)

    def exec(self) -> None:
        self._gen_training_list()
        self._gen_testing_list()
