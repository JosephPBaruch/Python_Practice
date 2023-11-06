#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:36:19 2023

@author: joseph.baruch
"""

import os
import PIL
import numpy as np

# create image object
my_img = PIL.Image.open('dog_image.jpg')
 # Add '.convert("L")' and it converts the image automatically to grayscale
 # The below code converts to grayscale

# display image
# my_img.show()

img_array = np.asarray(my_img)

# ITU-R 601-2 luma transform
# Eq: (.21 x R), (.72 x G), (.07 x B)

img_array.shape # See the dimensions of the array

# initalize a new array (2D) and its values
new_array = np.full((img_array.shape[0], img_array.shape[1]), 0, dtype=np.uint8)

'''' This is duplicated below in a more efficient way
for i in range(img_array.shape[0]):
    for j in range(img_array.shape[1]):
        R = img_array[i, j , 0]
        G = img_array[i, j , 1]
        B = img_array[i, j , 2]
        gray = (R * .299) + (G * .587) + (B * 0.114)
        lum_val = round(gray)
        new_array[i, j] = lum_val
'''
             
# display image that is not a PIL object but it is a 2D array      
# PIL.Image.fromarray(new_array).show() 

def grayscale_c(img):
    img_array = np.asarray(img)
    gray_img = np.full((img_array.shape[0], img_array.shape[1]), 0, dtype=np.uint8)
    R = img_array[:, : , 0]
    G = img_array[:, : , 1]
    B = img_array[:, : , 2]
    gray = (R * .299) + (G * .587) + (B * 0.114)
    final_gray = np.round(gray).astype(np.uint8)
    gray_img[:, :] = final_gray
    output_img = PIL.Image.fromarray(gray_img)
    return output_img
    
# ultralytics ( later down the road and something to look forward to)
new_img = grayscale_c(img_array)
# ------ Resize an Image -------
new_img = my_img.resize((255, 255), resample=PIL.Image.BILINEAR)
    