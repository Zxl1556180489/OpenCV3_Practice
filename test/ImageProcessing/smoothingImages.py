# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

def imageFiltering():
    img = cv2.imread('../../img/opencv.jpg')

    kernel = np.ones((7, 7), np.float32) / 49
    dst = cv2.filter2D(img, -1, kernel)

    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()

def imageBlurring():
    img = cv2.imread('../../img/wallhaven.jpg')

    # Averaging
    # blur = cv2.blur(img, (5, 5))
    # blur2 = cv2.blur(img, (11, 11))
    # blur3 = cv2.blur(img, (21, 21))

    # Gaussian Blurring
    # blur = cv2.GaussianBlur(img, (5, 5), 0)
    # blur2 = cv2.GaussianBlur(img, (11, 11), 0)
    # blur3 = cv2.GaussianBlur(img, (21, 21), 0)

    # median blurring
    # blur = cv2.medianBlur(img, 5)
    # blur2 = cv2.medianBlur(img, 11)
    # blur3 = cv2.medianBlur(img, 21)

    # bilateral blurring
    blur = cv2.bilateralFilter(img, 9, 75, 75)
    blur2 = cv2.bilateralFilter(img, 9, 125, 125)
    blur3 = cv2.bilateralFilter(img, 9, 175, 175)

    plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)), plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(cv2.cvtColor(blur2, cv2.COLOR_BGR2RGB)), plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(cv2.cvtColor(blur3, cv2.COLOR_BGR2RGB)), plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()

imageFiltering()
# imageBlurring()