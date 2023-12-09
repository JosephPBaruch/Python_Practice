#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:43:37 2023

@author: joseph.baruch
"""

import PIL
import numpy as np
import matplotlib.pyplot as plt

def convolution(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    
    # calculate the output shape
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1
    
    # define the output array
    output = np.zeros((output_height, output_width))
    
    for i in range(output_height):
        for j in range(output_width):
            output[i, j] = np.sum(image[i:i+kernel_height, j:j+kernel_width] * kernel) 
    return output

sobel_x = np.array([[-1, 0, 1], 
                    [-2, 0, 2], 
                    [-1, 0, 1]])

sobel_y = np.array([[-1, -2, -1], 
                    [ 0,  0, 0], 
                    [ 1,  2, 1]])

my_img = PIL.Image.open('dog_image.jpg').convert("L").resize((255,255), resample=PIL.Image.BILINEAR)
img_array = np.asarray(my_img)

x_out = convolution(img_array, sobel_x)
y_out = convolution(img_array, sobel_y)

final_output = np.sqrt(x_out**2 + y_out**2)

final_output[final_output < 170] = 0
final_output[final_output >= 170] = 255
final_output = final_output.astype(np.uint8)

final_img = PIL.Image.fromarray(final_output)

# plt.imshow(x_out)

# plt.imshow(y_out)

plt.imshow(final_output)

plt.imshow(final_img)