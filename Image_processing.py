# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:24:23 2024

@author: sreekar


"""
import cv2

# Read the image
img = cv2.imread("I'm too attractive_ Can't help.jpeg")

# Check if image is loaded properly
if img is None:
    print("Error: Could not read the image file.")
    exit()

# Create CLAHE object
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

# Convert to grayscale
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply CLAHE
enhancedimage = clahe.apply(grayimg)

# Save the enhanced image
cv2.imwrite('enhanced.jpeg', enhancedimage)

print('done!!')
