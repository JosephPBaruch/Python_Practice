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
import cv2 as cv

image = cv.imread('low.webp') # open 
resized = cv.resize(image, (256, 256)) # resize
#cv.imshow('Resized', resized) # display image
#cv.waitKey(0)   
gray_image = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)  # grayscale
#cv.imshow('Grayscale', gray_image) # display image
#cv.waitKey(0)   

# -------------- Canny Edge Detection -----------------
edges = cv.Canny(image=resized, threshold1=100, threshold2=200) 
 
#cv.imshow('Canny Edge Detection', edges)
#cv.waitKey(0)

# -------------- Histogram Equalization (HE) ----------------
equ = cv.equalizeHist(gray_image)

#cv.imshow('Historgram Equalization', equ)
#cv.waitKey(0)

# ------------- After HE Edge Detection --------
final = cv.Canny(image=equ, threshold1=100, threshold2=200) 
 
cv.imshow('Edge Detection with Histogram Equal.', final)
cv.waitKey(0)

cv.destroyAllWindows()


























