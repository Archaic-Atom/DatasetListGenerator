# -*- coding: utf-8 -*-
import os
from ._meta_stereo_ops import MetaStereoOps


class ETH3DStereoList(MetaStereoOps):
    TRAIN_FOLDER_LIST = ['delivery_area_1l', 'delivery_area_1s',
                         'delivery_area_2l', 'delivery_area_2s',
                         'delivery_area_3l', 'delivery_area_3s',
                         'electro_1l', 'electro_1s',
                         'electro_2l', 'electro_2s',
                         'electro_3l', 'electro_3s',
                         'facade_1s', 'forest_1s',
                         'forest_2s', 'playground_1l',
                         'playground_1s', 'playground_2l',
                         'playground_2s', 'playground_3l',
                         'playground_3s', 'terrace_1s',
                         'terrace_2s', 'terrains_1l',
                         'terrains_1s', 'terrains_2l',
                         'terrains_2s']

    VAL_FOLDER_LIST = ['lakeside_1l', 'lakeside_1s', 'sand_box_1l',
                       'sand_box_1s', 'storage_room_1l',
                       'storage_room_1s', 'storage_room_2_1l',
                       'storage_room_2_1s', 'storage_room_2_2l',
                       'storage_room_2_2s', 'storage_room_2l',
                       'storage_room_2s', 'storage_room_3l',
                       'storage_room_3s', 'tunnel_1l',
                       'tunnel_2l', 'tunnel_2s', 'tunnel_1s',
                       'tunnel_3l', 'tunnel_3s']

    def __init__(self, dataset_folder_path: str, save_folder_path: str) -> None:
        super().__init__(dataset_folder_path, save_folder_path)
        self._training_list = 'eth3d_stereo_training_list.csv'
        self._testing_list = 'eth3d_stereo_testing_list.csv'

    def _gen_training_list(self) -> None:
        file_num, off_set = 0, 1
        fd_file = self._open_file(os.path.join(self.save_folder_path, self._training_list))
        for folder_item in self.TRAIN_FOLDER_LIST:
            left_img_path = os.path.join(
                self.dataset_folder_path, 'two_view_training', folder_item, 'im0.png')
            right_img_path = os.path.join(
                self.dataset_folder_path, 'two_view_training', folder_item, 'im1.png')
            disp_path = os.path.join(
                self.dataset_folder_path, 'two_view_training_gt', folder_item, 'disp0GT.pfm')
            if not self._check_file_path(left_img_path, right_img_path, disp_path):
                break

            self.write_file(fd_file, f'{left_img_path},{right_img_path},{disp_path}')
            file_num = file_num + off_set

        self.close_file(fd_file)
        print('total file: ', file_num, '. The file has saved to ',
              os.path.join(self.save_folder_path, self._training_list))

    def _gen_testing_list(self) -> None:
        file_num, off_set = 0, 1
        fd_file = self._open_file(os.path.join(self.save_folder_path, self._testing_list))
        for folder_item in self.VAL_FOLDER_LIST:
            left_img_path = os.path.join(
                self.dataset_folder_path, 'two_view_test', folder_item, 'im0.png')
            right_img_path = os.path.join(
                self.dataset_folder_path, 'two_view_test', folder_item, 'im1.png')
            disp_path = None

            if not self._check_file_path(
                    left_img_path, right_img_path, disp_path, is_training=False):
                break

            self.write_file(fd_file, f'{left_img_path},{right_img_path},{disp_path}')
            file_num = file_num + off_set

        self.close_file(fd_file)
        print('total file: ', file_num, '. The file has saved to ',
              os.path.join(self.save_folder_path, self._testing_list))

    def exec(self) -> None:
        self._gen_training_list()
        self._gen_testing_list()
