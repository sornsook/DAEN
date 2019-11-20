# The Density-Aware Estimation Network (DAEN)

This is an official implementation of SITIS 2019 paper "The Density-Aware Estimation Network for Vehicle Counting in Traffic Surveillance System" which can be read in the following link:
xxxxxxxxxxxxxxxxxxxxx.com (not avaiable yet)

# Installation
1. Install tensorflow (and keras)
2. git clone https://github.com/sornsook/DAEN.git

# Data setup
Download dataset from 'xxxxxxxxxx.com' into 'Npy_file' consisting of:
   - Train_images.npy:  The input images for training
   - Train_labels.npy:  The density maps for training
   - Val_images.npy:    The input images for validation 
   - Val_labels.npy:    The density maps for validation
   
   *The traffic images have already converted into .npy files.*
   *The original images can be found in TRANCOS dataset (http://agamenon.tsc.uah.es/Personales/rlopez/data/trancos/)*

# Train
run python3 Backward_network_training.py. \
model weights are saved to 'saved_weight/slave_network' and 'saved_weight/master_network'

# Test
run python3 Backward_network_testing.py. \
The mean absolute error (MAE) are saved to 'experimental_results/backward.csv'. \
The output images are saved to 'output_images/'


**FYI:Please note that this code is run by Tensorflow 1.0.**


