# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt


def showEdge():
    img = cv2.imread('../../img/opencv.jpg', 0)
    edges = cv2.Canny(img, 100, 200)

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()


def nothing(x):
    pass


def showEdgeWithTrackBar():
    img = cv2.imread('../../img/sudoku.jpg', 0)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.createTrackbar('MinValue', 'image', 100, 255, nothing)
    cv2.createTrackbar('MaxValue', 'image', 200, 255, nothing)
    while (1):
        key = cv2.waitKey(1)

        if key & 0xFF == ord('q'):
            break

        # get current positions of four trackbars
        minValue = cv2.getTrackbarPos('MinValue', 'image')
        maxValue = cv2.getTrackbarPos('MaxValue', 'image')
        print minValue, maxValue

        edges = cv2.Canny(img, minValue, maxValue)
        cv2.imshow('image', edges)

    cv2.destroyAllWindows()


# showEdge()
showEdgeWithTrackBar()
