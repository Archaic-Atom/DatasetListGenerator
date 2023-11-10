# DataloaderListGenertor
### Software Environment
1. **OS Environment**  
```
$ os >= linux 16.04  
$ cudaToolKit >= 10.1  
$ cudnn >= 7.3.6  
```
2. **Python Environment**  
```
$ python >= 3.8.5  
$ pythorch >= 1.15.0  
$ numpy >= 1.14.5   
$ PIL >= 5.1.0
```
***
### Software Environment
This framework is only used in Linux.
***


### How to use our DataloaderListGenertor:
1. **Install the DataloaderListGenertor lib**  
```
$ ./bulid.sh
```

2. **How to use the DataloaderListGenertor**  
```
$ DatasetListGenerator --task "stereo matching" --dataset "SceneFlow" --dataset_folder_path /data/datasets/StereoMatching/SceneFlow/ --save_folder_path ./
```

3. **parameter information**
   * **--task**  
   default=stereo matching

   * **--dataset**  
   default='KITTI2012'   

   **Other Parameters**  
   **Parameters** |**Description**  
   :-         | :-            
   'WHUStereo' | WHUStereoList 
   'CREStereo' | CreStereoLis   
   'KITTI2012' |KITTI2012StereoList  
   'KITTI2015':|KITTI2015StereoList  
   'ETH3D'    |ETH3DStereoList 
   'Middlebury'| MiddleburyStereoList   
   'US3D'      |US3DStereoList  
   'SceneFlow' |SceneFlowStereoList
   

   *  **--dataset_folder_path**  
   your datasets path
   *  **--save_folder_path**  
   The path where your.csv file is saved.
4. **Clean the project (if you want to clean generating files)**
   ```
   $ ./clean.sh
   ```
***
### File Structure
```
DataloaderListGenertor
├── Source # source code
│   ├──setup.py
│   └── DataloaderListGenertor/
│       ├── Reconstruction/
│       ├── Stereo/
│       ├── SysBasic/
│       ├── Template/
│       └── main.py 
├── Scripts/
│   ├── gen_stereo_list.sh
│   ├── install.sh
│   └── ...
├── Example/ 
│   ├── whu_stereo_training_list.csv
│   └── ...
├── LICENSE
├── build.sh 
├── clean.sh 
└── README.md
```
***
### Update log
2023-11-02
   1. Write the ReadMe.