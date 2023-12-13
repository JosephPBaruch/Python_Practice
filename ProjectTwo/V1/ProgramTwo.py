import cv2
from ultralytics import YOLO
import ultralytics
ultralytics.checks()
import os
import PIL
import albumentations as A
os. chdir('/Users/joseph.baruch/REPO/Practical_Python/ProjectTwo/V1') 

train_path = './data/train/coniferous/'
test_path = './data/test/coniferous/'
val_path = './data/val/coniferous/'

train_path2 = './data/train/desert/'
test_path2 = './data/test/desert/'
val_path2 = './data/val/desert/'

train_path3 = './data/train/grassland/'
test_path3 = './data/test/grassland/'
val_path3 = './data/val/grassland/'

train_path4 = './data/train/rain_forest/'
test_path4 = './data/test/rain_forest/'
val_path4 = './data/val/rain_forest/'

train_path5 = './data/train/tundra/'
test_path5 = './data/test/tundra/'
val_path5 = './data/val/tundra/'

path_lists = [train_path, test_path, val_path,
              train_path2, test_path2, val_path2,
              train_path3, test_path3, val_path3,
              train_path4, test_path4, val_path4,
              train_path5, test_path5, val_path5]

def resize():
    for path in path_lists:
        file_list = os.listdir(path)
        file_list = [file for file in file_list if '.webp' in file]
        for file in file_list:
            img = PIL.Image.open(path + file)
            img = img.resize((512, 512))
            img.save(path + file)

def augment_and_add():
    d

model = YOLO("yolov8n-cls.pt")
model.train(data='./data', epochs=200)


