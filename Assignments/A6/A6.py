#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Joseph Baruch
CS 212: Practical Python
Assignment 6: Histogram Equalization and Line Detection with OpenCV
Description: 
    1.) Find a low contrast image;
    2.) Transform this image to grayscale and resize the image to (256, 256); 
    3.) Perform edge detection on the image;
    4.) On the grayscale image, perform histogram equalization and then perform 
        edge detection again. ONLY USE OpenCV methods!
"""

#import PIL
#import os
#import numpy as np
#import matplotlib.pyplot as plt
import cv2 as cv
# low.webp
# read image

 # new_img = new_img.resize((255, 255), resample=PIL.Image.BILINEAR)
 # new_img = grayscale_c(img_array)
#my_img = PIL.Image.open('low.webp').convert('L') # Convert to 
#my_img.show()

image = cv.imread('low.webp')
#cv.imshow('Original', image) 
#cv.waitKey(0)

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) 
  
cv.imshow('Grayscale', gray_image) 
cv.waitKey(0)   
  
# Window shown waits for any key pressing event 
cv.destroyAllWindows()
"""
# convert image object to an array
im_array = np.asarray(my_img)
# flatten to a 1D array
hist_array = im_array.flatten()
# generate the histogram
hist, _ = np.histogram(hist_array, 256, [0, 255])
# calculate the CDF
cdf = hist.cumsum()
# normalize the distribution to be between 0 and 255
cdf_normalized = ((cdf - cdf.min()) / (cdf.max() - cdf.min())) * 255
# map our original pixels to the new distribution
result = cdf_normalized[hist_array]
# reshape back to a 2D array
final_result = np.reshape(result, im_array.shape)
# visualize the distributions (before and after)
plt.hist(result.flatten(), color='green', ec='black')
plt.hist(hist_array, color='skyblue', ec='black')
plt.xlabel('Pixel Intensity')
plt.ylabel('Pixel Count')
plt.show()
# perform the same method using OpenCV
image = cv.imread('lowContrast.png', cv.IMREAD_GRAYSCALE)
equ = cv.equalizeHist(image)
equ_hist_arr = equ.flatten()
plt.hist(equ_hist_arr, color = "bisque", ec='black')
plt.xlabel('Intensity')
plt.ylabel('Count')
plt.title('Histogram Equalized')
plt.show()
"""