import sys
import sklearn
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
import os
import scipy
import pandas as pd
import scipy.io as sio
import tensorflow as tf
import numpy as np
import time
import math
import pdb
import h5py

file_list = ["s01", "s02","s03","s04","s05","s06","s07","s08","s09","s10", "s11", "s12", "s13", "s14", "s15", "s16", "s17", "s18", "s19", "s20", "s21", "s22", "s23", "s24", "s25", "s26", "s27", "s28", "s29", "s30", "s31", "s32"]

'''
data_file = sio.loadmat("./merged_file_all.mat")
#data_file = sio.loadmat("./DE_CNN/3D_dataset/with_base/DE_s01.mat")
for key, value in data_file.items():
    print(key, len(value))
label = data_file["valence_labels"]
print(label)
print(len(label))
print(label.shape)
print(data_file["data"].shape)

#new_label = np.hstack(label)
new_label = label.reshape(1, -1)
print(new_label)
print(new_label.shape)

#print(np.isnan(data_file["data"]))

new_label1 = data_file["arousal_labels"].reshape(1, -1)

for elem in new_label:
    for element in elem:
        #print(element)
        if(np.isnan(element)):
            print("*****There is nan value*****")
            break

for elem in new_label1:
    for element in elem:
        #print(element)
        if(np.isnan(element)):
            print("*****There is nan value*****")
            break

for elem in data_file["data"]:
    for element in elem:
        for elem1 in element:
            for elem2 in elem1:
                #print(elem2)
                if(np.isnan(elem2)):
                    print("*****There is nan value*****")
                    break

    


# Load data from all .mat files and merge

'''
input_list = ["./DE_CNN/3D_dataset/with_base/DE_s09.mat", "./DE_CNN/3D_dataset/with_base/DE_s10.mat"
, "./DE_CNN/3D_dataset/with_base/DE_s11.mat", "./DE_CNN/3D_dataset/with_base/DE_s12.mat", "./DE_CNN/3D_dataset/with_base/DE_s13.mat", "./DE_CNN/3D_dataset/with_base/DE_s14.mat", "./DE_CNN/3D_dataset/with_base/DE_s15.mat", "./DE_CNN/3D_dataset/with_base/DE_s16.mat"]
merged_data = {}
for file in input_list:
    #file = "./DE_CNN/3D_dataset/with_base/DE_" + file + ".mat"
    data = sio.loadmat(file)
    if not merged_data:
        merged_data = data
    else:
        for key in data.keys():
            if key in merged_data:
                #print("key:", key)
                if key == "__header__" or key == "__version__" or key == "__globals__":
                    continue
                # Concatenate arrays along the 0 axis
                merged_data[key] = np.concatenate((merged_data[key], data[key]), axis=0)
            else:
                # Add new key-value pair to merged_data
                merged_data[key] = data[key]

# Save merged data to new .mat file
sio.savemat('merged_file_(9to16).mat', merged_data)
