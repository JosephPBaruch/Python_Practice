import cv2
from ultralytics import YOLO
import ultralytics
ultralytics.checks()
import os
import PIL
# import albumentations as A
os. chdir('/Users/joseph.baruch/REPO/Practical_Python/ProjectTwo/V1') 

new_model = YOLO('./runs/classify/train6/weights/best.pt')
path = './test/'

def resize(): 
    file_list = os.listdir(path)
    file_list = [file for file in file_list if '.jpeg' or '.png' or '.jpg' in file]
    for file in file_list:
        img = PIL.Image.open(path + file)
        img = img.resize((512, 512))
        img.save(path + file)

def predict():
    file_list = os.listdir(path)
    file_list = [file for file in file_list if '.jpeg' or '.png' or '.jpg' in file]
    for file in file_list:
        new_model(path + file)

# resize()
predict()

''' Epoch 60 (train4): 
        - 1 Coniferous:    coniferous 0.95, rain_forest 0.03, desert 0.01, tundra 0.01, grassland 0.00
        - 2 Desert:        grassland 0.43, tundra 0.38, desert 0.17, coniferous 0.02, rain_forest 0.01
        - 3 Grassland:     grassland 0.97, tundra 0.02, coniferous 0.01, desert 0.00, rain_forest 0.00
        - 4 Rain Forest:   rain_forest 1.00, coniferous 0.00, desert 0.00, tundra 0.00, grassland 0.00
        - 5 Tundra:        tundra 1.00, desert 0.00, coniferous 0.00, grassland 0.00, rain_forest 0.00
'''
''' Epoch 200 (train5): 
        - 1 Coniferous:    coniferous 0.97, rain_forest 0.02, desert 0.00, tundra 0.00, grassland 0.00 
        - 2 Desert:        grassland 0.51, tundra 0.30, desert 0.16, coniferous 0.03, rain_forest 0.01
        - 3 Grassland:     grassland 0.99, tundra 0.01, coniferous 0.00, desert 0.00, rain_forest 0.00
        - 4 Rain Forest:   rain_forest 1.00, desert 0.00, coniferous 0.00, tundra 0.00, grassland 0.00
        - 5 Tundra:        tundra 1.00, desert 0.00, coniferous 0.00, rain_forest 0.00, grassland 0.00
'''
''' Epoch 200 (train6) with Augmentations: 
        - Coniferous:      coniferous 0.49, rain_forest 0.48, desert 0.03, grassland 0.00, tundra 0.00
        - Desert:          grassland 0.60, desert 0.26, coniferous 0.10, tundra 0.04, rain_forest 0.00 
        - Grassland:       grassland 1.00, tundra 0.00, coniferous 0.00, desert 0.00, rain_forest 0.00
        - Rain Forest:     rain_forest 1.00, coniferous 0.00, tundra 0.00, desert 0.00, grassland 0.00
        - Tundra:          tundra 1.00, desert 0.00, coniferous 0.00, rain_forest 0.00, grassland 0.00
'''
''' Epoch 200 (train6) with Augmentations: 
        - Coniferous:      
        - Desert:          
        - Grassland:       
        - Rain Forest:     
        - Tundra:          
'''