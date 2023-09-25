# -*- coding: utf-8 -*-
import os
from ._meta_stereo_ops import MetaStereoOps


class MiddleburyStereoList(MetaStereoOps):
    TRAIN_FOLDER_LIST = ['Adirondack', 'Jadeplant', 'MotorcycleE', 'PianoL',
                         'Playroom', 'PlaytableP', 'Shelves', 'Vintage',
                         'ArtL', 'Motorcycle', 'Piano', 'Pipes',
                         'Playtable', 'Recycle', 'Teddy']

    VAL_FOLDER_LIST = ['Australia', 'Bicycle2', 'Classroom2E', 'Crusade',
                       'Djembe', 'Hoops', 'Newkuba', 'Staircase',
                       'AustraliaP', 'Classroom2', 'Computer', 'CrusadeP',
                       'DjembeL', 'Livingroom', 'Plants']

    def __init__(self, dataset_folder_path: str, save_folder_path: str) -> None:
        super().__init__(dataset_folder_path, save_folder_path)
        self._training_list = 'eth3d_stereo_training_list.csv'
        self._testing_list = 'eth3d_stereo_testing_list.csv'

    def _gen_training_list(self) -> None:
        file_num, off_set = 0, 1
        fd_file = self._open_file(os.path.join(self.save_folder_path, self._training_list))
        for folder_item in self.TRAIN_FOLDER_LIST:
            left_img_path = os.path.join(
                self.dataset_folder_path, 'trainingH/', folder_item, 'im0.png')
            right_img_path = os.path.join(
                self.dataset_folder_path, 'trainingH/', folder_item, 'im1.png')
            disp_path = os.path.join(
                self.dataset_folder_path, 'trainingH/', folder_item, 'disp0GT.pfm')

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

        for folder_item in self.VAL_FOLDER_LIST:
            left_img_path = os.path.join(self.dataset_folder_path, 'testH/', folder_item, 'im0.png')
            right_img_path = os.path.join(self.dataset_folder_path, 'testH/', folder_item, 'im1.png')
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
