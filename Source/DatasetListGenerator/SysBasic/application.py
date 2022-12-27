# -*- coding: UTF-8 -*-
from DatasetListGenerator.Stereo import stereo_dataset_selection
from .args_parser import ArgsParser


class Application(object):
    __APPLICATION = None

    def __init__(self) -> None:
        super().__init__()

    def __new__(cls, *args: str, **kwargs: str) -> object:
        if cls.__APPLICATION is None:
            cls.__APPLICATION = object.__new__(cls)
        return cls.__APPLICATION

    def start(self) -> None:
        args = ArgsParser().parse_args()
        cls_generator = self._get_dataset_selection(args.task)(args.dataset)
        generator = cls_generator(args.dataset_folder_path, args.save_folder_path)
        generator.exec()

    def _get_task_func_dict(self) -> dict:
        return {'stereo matching': stereo_dataset_selection}

    def _get_dataset_selection(self, task: str) -> object:
        task_func_dict = self._get_task_func_dict()
        return task_func_dict[task]
