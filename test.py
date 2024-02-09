#convert pickle to json

import pickle
import json

path = '/homes/kasper/Documents/Totalsegmentator/nnUNet_trained_models/Dataset993_BAT/nnUNetTrainerV2_ep4000_nomirror__nnUNetPlans__3d_fullres/plans.pkl'
with open(path, 'rb') as f:
    data = pickle.load(f)

path = '/homes/kasper/Documents/Totalsegmentator/nnUNet_trained_models/Dataset993_BAT/nnUNetTrainerV2_ep4000_nomirror__nnUNetPlans__3d_fullres/plans.json'
with open(path, 'w') as f:
    json.dump(data, f, indent=4)