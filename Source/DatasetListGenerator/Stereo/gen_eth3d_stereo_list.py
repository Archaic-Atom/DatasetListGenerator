# -*- coding: utf-8 -*-
import os
from ._meta_stereo_ops import MetaStereoOps


class ETH3DStereoList(MetaStereoOps):
    TRAIN_FOLDER_LIST = ['TRAIN/delivery_area_1l', 'TRAIN/delivery_area_1s',
                         'TRAIN/delivery_area_2l', 'TRAIN/delivery_area_2s',
                         'TRAIN/delivery_area_3l', 'TRAIN/delivery_area_3s',
                         'TRAIN/electro_1l', 'TRAIN/electro_1s',
                         'TRAIN/electro_2l', 'TRAIN/electro_2s',
                         'TRAIN/electro_3l', 'TRAIN/electro_3s',
                         'TRAIN/facade_1s', 'TRAIN/forest_1s',
                         'TRAIN/forest_2s', 'TRAIN/playground_1l',
                         'TRAIN/playground_1s', 'TRAIN/playground_2l',
                         'TRAIN/playground_2s', 'TRAIN/playground_3l',
                         'TRAIN/playground_3s', 'TRAIN/terrace_1s',
                         'TRAIN/terrace_2s', 'TRAIN/terrains_1l',
                         'TRAIN/terrains_1s', 'TRAIN/terrains_2l',
                         'TRAIN/terrains_2s']

    VAL_FOLDER_LIST = ['TEST/lakeside_1l', 'TEST/lakeside_1s', 'TEST/sand_box_1l',
                       'TEST/sand_box_1s', 'TEST/storage_room_1l',
                       'TEST/storage_room_1s', 'TEST/storage_room_2_1l',
                       'TEST/storage_room_2_1s', 'TEST/storage_room_2_2l',
                       'TEST/storage_room_2_2s', 'TEST/storage_room_2l',
                       'TEST/storage_room_2s', 'TEST/storage_room_3l',
                       'TEST/storage_room_3s', 'TEST/tunnel_1l',
                       'TEST/tunnel_2l', 'TEST/tunnel_2s', 'TEST/tunnel_1s',
                       'TEST/tunnel_3l', 'TEST/tunnel_3s']

    def __init__(self, dataset_folder_path: str, save_folder_path: str) -> None:
        super().__init__(dataset_folder_path, save_folder_path)
        self._training_list = 'eth3d_stereo_training_list.csv'
        self._testing_list = 'eth3d_stereo_testing_list.csv'

    def _gen_training_list(self) -> None:
        file_num, off_set = 0, 1
        fd_file = self._open_file(os.path.join(self.save_folder_path, self._training_list))
        for folder_item in self.TRAIN_FOLDER_LIST:
            left_img_path = os.path.join(self.dataset_folder_path, folder_item, 'im0.png')
            right_img_path = os.path.join(self.dataset_folder_path, folder_item, 'im1.png')
            disp_path = os.path.join(self.dataset_folder_path, folder_item, 'disp0GT.pfm')

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
        for folder_item in self.VAL_FOLDER_LIST:
            left_img_path = os.path.join(self.dataset_folder_path, folder_item, 'im0.png')
            right_img_path = os.path.join(self.dataset_folder_path, folder_item, 'im1.png')
            disp_path = None

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
