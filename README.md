# The Density-Aware Estimation Network (DAEN)

This is an official implementation of SITIS 2019 paper "The Density-Aware Estimation Network for Vehicle Counting in Traffic Surveillance System" which can be read in our published paper as follows:\
" S. Sooksatra, A. Yoshitaka, T. Kondo, and P. Bunnun, The Density-Aware Estimation
Network for Vehicle Counting in Traffic Surveillance System, The 15 th International
Conference on Signal Image Technology & Internet Based Systems, pp. 231-238, 26-29
November 2019, Sorrento, Italy. "

# Installation
1. Install tensorflow (and keras)
2. git clone https://github.com/sornsook/DAEN.git

# Data setup
Download dataset from 'https://drive.google.com/open?id=1ppSJMunUMNI1RO8ZvgIwBNH9bh1NEK03' into 'Npy_file' consisting of:
   - Train_images.npy:  The input images for training
   - Train_labels.npy:  The density maps for training
   - Test_images.npy:    The input images for testing 
   - Test_labels.npy:    The density maps for testing
   
   *The traffic images have already converted into .npy files.*
   *The original images can be found in TRANCOS dataset (http://agamenon.tsc.uah.es/Personales/rlopez/data/trancos/)*

# Train
run 'Backward-network_training.ipynb' via jupyter notebook. \
model weights are saved to 'saved_weight/slave_network' and 'saved_weight/master_network'

# Test
run 'Backward-network_testing.ipynb' via jupyter notebook. \
The mean absolute error (MAE) are saved to 'Experimental_result/backward.csv'. \
The output images are saved to 'Output_image/'


**FYI:Please note that this code is run by Tensorflow 1.0.**


