# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../../img/j.png', 0)
imgClosing = cv2.imread('../../img/j-closing.png', 0)
imgOpening = cv2.imread('../../img/j-opening.png', 0)
kernel = np.ones((5, 5), np.uint8)

def erosion():
    return cv2.erode(img, kernel, iterations=1)

def dilation():
    return cv2.dilate(img, kernel, iterations=1)

def opening():
    return cv2.morphologyEx(imgOpening, cv2.MORPH_OPEN, kernel)

def closing():
    return cv2.morphologyEx(imgClosing, cv2.MORPH_CLOSE, kernel)

def morphologicalGradient():
    return cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

def topHat():
    kernel = np.ones((9, 9), np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

def blackHat():
    kernel = np.ones((7, 7), np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

def showPlot1():
    plt.subplot(231), plt.imshow(img, cmap = 'gray'), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(232), plt.imshow(erosion(), cmap = 'gray'), plt.title('Erosion')
    plt.xticks([]), plt.yticks([])
    plt.subplot(233), plt.imshow(dilation(), cmap = 'gray'), plt.title('Dilation')
    plt.xticks([]), plt.yticks([])

    plt.subplot(234), plt.imshow(morphologicalGradient(), cmap = 'gray'), plt.title('Morphological Gradient')
    plt.xticks([]), plt.yticks([])
    plt.subplot(235), plt.imshow(topHat(), cmap = 'gray'), plt.title('Top Hat')
    plt.xticks([]), plt.yticks([])
    plt.subplot(236), plt.imshow(blackHat(), cmap = 'gray'), plt.title('Black Hat')
    plt.xticks([]), plt.yticks([])
    plt.show()

def showPlot2():
    plt.subplot(221), plt.imshow(imgOpening, cmap = 'gray'), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(opening(), cmap = 'gray'), plt.title('Opening')
    plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(imgClosing, cmap = 'gray'), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(closing(), cmap = 'gray'), plt.title('Closing')
    plt.xticks([]), plt.yticks([])
    plt.show()

showPlot1()
# showPlot2()
