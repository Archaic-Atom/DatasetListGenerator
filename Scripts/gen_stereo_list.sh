#!/bin/bash
python ./Source/main.py --task "stereo matching" --dataset WHUStereo --dataset_folder_path '/Users/rhc/Downloads/Dataset/experimental data/with ground truth/' --save_folder_path "./Example/"
python ./Source/main.py --task "stereo matching" --dataset CREStereo --dataset_folder_path '/home3/datasets/raozhibo/CRE_Stereo/stereo_trainset/crestereo/' --save_folder_path "./Example/"