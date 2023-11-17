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
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # grayscale
resized = cv.resize(gray_image, (256, 256)) # resize
#cv.imshow('Resized', resized) # display image
#cv.waitKey(0)   

# -------------- Sobel Edge Detection ---------------
sobelx = cv.Sobel(src=resized, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv.Sobel(src=resized, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv.Sobel(src=resized, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
 
#cv.imshow('Sobel X', sobelx)
#cv.waitKey(0)
 
#cv.imshow('Sobel Y', sobely)
#cv.waitKey(0)
 
#cv.imshow('Sobel X Y using Sobel() function', sobelxy)
#cv.waitKey(0)

# -------------- Canny Edge Detection -----------------
edges = cv.Canny(image=resized, threshold1=100, threshold2=200) 
 
#cv.imshow('Canny Edge Detection', edges)
#cv.waitKey(0)

# -------------- Histogram Equalization (HE) ----------------
equ = cv.equalizeHist(resized)

#cv.imshow('Historgram Equalization', equ)
#cv.waitKey(0)

# ------------- After HE Edge Detection --------
final = cv.Canny(image=equ, threshold1=100, threshold2=200) 
 
cv.imshow('Canny Edge Detection', final)
cv.waitKey(0)












cv.destroyAllWindows()


























