# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

# flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# print flags

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    frame = cv2.flip(frame, flipCode=1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_red = np.array([170,60,20])
    upper_red = np.array([179,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    key = cv2.waitKey(1)

    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()