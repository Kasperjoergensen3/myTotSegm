from pathlib import Path
import shutil
from totalsegmentator.libs import get_config_dir


# Specify the trained model
CONFIGURATION = '3d_fullres'
TASK_NAME = 'Task993_BAT'
TRAINER_CLASS = 'nnUNetTrainerV2_ep4000_nomirror__nnUNetPlansv2.1'
FOLD = 'fold_5'
trained_model_path = Path('nnUNet_trained_models/nnUNet').joinpath(CONFIGURATION, TASK_NAME, TRAINER_CLASS)

# make name for model folder
no_subjects_in_training = 159
model_folder = f"{TASK_NAME}_{no_subjects_in_training}subj"


# get weights directory
# something like /home/username/.totalsegmentator/nnunet/results/nnUNet/3d_fullres/Task993_BAT_159subj/nnUNetTrainerV2_ep4000_nomirror__nnUNetPlansv2.1
totalsegmentator_weights_dir = Path(get_config_dir().joinpath(CONFIGURATION, model_folder, TRAINER_CLASS))

# copy model in local folder to model in Totalsegmentator weights folder
shutil.copytree(trained_model_path, totalsegmentator_weights_dir)

# copy the latest model checkpoint to the final model checkpoint (for fold 5)
shutil.copy(totalsegmentator_weights_dir.joinpath(FOLD, 'model_latest.model'), totalsegmentator_weights_dir.joinpath(FOLD, 'model_final_checkpoint.model'))
shutil.copy(totalsegmentator_weights_dir.joinpath(FOLD, 'model_latest.model.pkl'), totalsegmentator_weights_dir.joinpath(FOLD, 'model_final_checkpoint.model.pkl'))


