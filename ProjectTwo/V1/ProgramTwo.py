import cv2
from ultralytics import YOLO
import ultralytics
ultralytics.checks()
import os
import PIL
import albumentations as A

os.chdir('/Users/joseph.baruch/REPO/Practical_Python/ProjectTwo/V1') 

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

def resize():
    for path in path_lists:
        file_list = os.listdir(path)
        file_list = [file for file in file_list if '.webp' in file]
        for file in file_list:
            img = PIL.Image.open(path + file)
            img = img.resize((512, 512))
            img.save(path + file)

transform = A.Compose([
    A.RandomCrop(width=512, height=512),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.ShiftScaleRotate(p=0.5)
])

def augment_and_add():
    for path in path_li:
        os.chdir('/Users/joseph.baruch/REPO/Practical_Python/ProjectTwo/V1' + path ) 
        file_list = os.listdir('/Users/joseph.baruch/REPO/Practical_Python/ProjectTwo/V1' + path)
        file_list = [file for file in file_list if '.webp' in file]
        for file in file_list:
            image = cv2.imread(file)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            transformed = transform(image=image)['image']
            cv2.imwrite('tran_' + file , transformed)
    os.chdir('/Users/joseph.baruch/REPO/Practical_Python/ProjectTwo/V1')

#resize()
#augment_and_add()


model = YOLO("yolov8n-cls.pt")
model.train(data='./data', epochs=200)


