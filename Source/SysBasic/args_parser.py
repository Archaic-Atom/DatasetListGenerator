# -*- coding: utf-8 -*-
import argparse


class ArgsParser(object):

    def __init__(self):
        super().__init__()

    def parse_args(self) -> object:
        parser = argparse.ArgumentParser(description="The dataset list generator")
        parser.add_argument('--task', default='stereo matching', help='the name of tasks')
        parser.add_argument('--dataset', default='kitti2012', help='the name of tasks')
        parser.add_argument('--dataset_folder_path', help='the path of dataset')
        parser.add_argument('--save_folder_path', help='the path of save_folder')
        return parser.parse_args()
