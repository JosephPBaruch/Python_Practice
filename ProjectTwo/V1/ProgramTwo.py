'''
    Joseph Baruch
    December 15, 2023
    Program Two: Image Classification
    Description: Prepare images by resizing and augmenting for the training 
    of Ultralytics YOLOV8 image classificaiton model yolov8n-cls.
'''
import cv2
from ultralytics import YOLO
import ultralytics
ultralytics.checks()
import os
import PIL
import albumentations as A

basePATH = '/Users/joseph.baruch/REPO/Practical_Python/ProjectTwo/V1'
os.chdir(basePATH) 

# Paths to different files for image preparations. 
train_1 = '/data/train/coniferous/'
test_1 = '/data/test/coniferous/'
val_1 = '/data/val/coniferous/'

train_2 = '/data/train/desert/'
test_2 = '/data/test/desert/'
val_2 = '/data/val/desert/'

train_3 = '/data/train/grassland/'
test_3 = '/data/test/grassland/'
val_3 = '/data/val/grassland/'

train_4 = '/data/train/rain_forest/'
test_4 = '/data/test/rain_forest/'
val_4 = '/data/val/rain_forest/'

train_5 = '/data/train/tundra/'
test_5 = '/data/test/tundra/'
val_5 = '/data/val/tundra/'

path_li = [train_1, test_1, val_1,
        train_2, test_2, val_2,
        train_3, test_3, val_3,
        train_4, test_4, val_4,
        train_5, test_5, val_5]

# Albumentations image augumentation pipline. 
transform = A.Compose([
    A.RandomCrop(width=512, height=512),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.ShiftScaleRotate(p=0.5)
])

def resize():
    '''
        Resize all images in data directory by traversing file structure. 
    '''
    for path in path_li:
        file_list = os.listdir(basePATH + path)
        file_list = [file for file in file_list if '.webp' in file]
        for file in file_list:
            img = PIL.Image.open(basePATH + path + file)
            img = img.resize((512, 512)) # Size of images changed to 512 x 512
            img.save(basePATH + path + file) # Save image as origional name

def augment_and_add():
    '''
        Augument images using predefined augumentation pipeline. 
        Traverse file structure in data directory like in 'resize()'
    '''
    for path in path_li:
        os.chdir(basePATH + path ) 
        file_list = os.listdir(basePATH + path)
        file_list = [file for file in file_list if '.webp' in file]
        for file in file_list:
            image = cv2.imread(file)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            transformed = transform(image=image)['image']
            cv2.imwrite('2_tran_' + file , transformed) # May need to adjust first string if multiple augmentation cycles
    os.chdir(basePATH)

resize()
augment_and_add()
model = YOLO("yolov8n-cls.pt") # Train model
model.train(data='./data', epochs=400)


