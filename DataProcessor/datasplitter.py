import os
import shutil
import split_folders

dir_train = 'car_data/train'
dir_test = 'car_data/test'
dir_all = 'car_data/Cars'
dir_out = 'car_data/output'

# os.makedirs(dir_all+"/"+i)

# Combining train and test datasets
dirs = os.listdir(dir_train)
for i in dirs:
    if i != ".DS_Store":
        shutil.copytree(dir_train + "/" + i, dir_all + "/" + i)

dirs = os.listdir(dir_test)
for i in dirs:
    if i != ".DS_Store":
        files = os.listdir(dir_test + "/" + i)
        for f in files:
            if f != ".DS_Store":
                shutil.copy(dir_test + "/" + i + "/" + f, dir_all + "/" + i)

# Splitting into train, test and validation sets
split_folders.ratio(dir_all, output=dir_out, seed=1337, ratio=(.8, .1, .1))

# Data number counting
# dirs_train = os.listdir(dir_train)
i = 0
for folder in os.listdir(dir_train):
    if folder != ".DS_Store":
        for f in os.listdir(dir_train + "/" + folder):
            if f.endswith(".jpg"):
                i += 1

for folder in os.listdir(dir_test):
    if folder != ".DS_Store":
        for f in os.listdir(dir_test + "/" + folder):
            if f.endswith(".jpg"):
                i += 1

print(i)
