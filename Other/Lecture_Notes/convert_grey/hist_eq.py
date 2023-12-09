#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:51:02 2023

@author: joseph.baruch
"""

import PIL 
import os 
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

my_img = PIL.Image.open('low_con.jpg').convert('L')

im_array = np.array(my_img)

hist_array = im_array.flatten()

hist, _ = np.histogram(hist_array, 256, [0,255])

# Cumulative Density Function (CDF)

cdf = hist.cumsum()

# normalize the cdf
cdf_normalized = ((cdf - cdf.min()) / (cdf.max() - cdf.min()))* 255

result = cdf_normalized[hist_array]

final_result = np.reshape(result, im_array.shape)

plt.hist(result.flatten(), color='green', ec='black')
plt.hist(hist_array, color='skyblue', ec='black')
plt.xlabel('Pixel Intensity')
plt.ylabel('Pixel Count')

# plt.show()

image = cv.imread('low_con.jpg', cs.IMREAD_GRAYSCALE) # need to import cv2 with pip

equ = cv.equalizeHist(image)

equ_hist_arr = equ.flatten()

# plot