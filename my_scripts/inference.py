#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from totalsegmentator.python_api import totalsegmentator
from pathlib import Path


INF_VERSION = 'v1'
TASK_NAME = 'my_BAT'
DATA_PATH = Path('DATA')
INFERENCE_PATH = Path('Inferences').joinpath(f"{TASK_NAME}_{INF_VERSION}")
CT_target = 'ct.nii.gz'
BAT_output = 'BAT.nii.gz'


for pt in DATA_PATH.iterdir():
    print('Performing inference... on subject: ', pt.name)
    
    # input ct path
    input_ct_path = pt.joinpath(CT_target)

    #output BAT segmentation path
    output_BAT_path = INFERENCE_PATH.joinpath(pt.name, BAT_output)
    output_BAT_path.parent.mkdir(parents=True, exist_ok=True)

    # perform inference using totalsegmentator API
    totalsegmentator(input_ct_path, output_BAT_path, task=TASK_NAME)



