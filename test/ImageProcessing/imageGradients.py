# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

def gradients():
    img = cv2.imread('../../img/sudoku.jpg', 0)

    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray', vmin = 0, vmax = 255)
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray', vmin = 0, vmax = 255)
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray', vmin = 0, vmax = 255)
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()

def gradients2():
    img = cv2.imread('../../img/box.png', 0)

    # Output dtype = cv2.CV_8U
    sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)

    # Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
    sobelx64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    abs_sobel64f = np.absolute(sobelx64f)
    sobel_8u = np.uint8(abs_sobel64f)

    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
    plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
    plt.subplot(1, 3, 3), plt.imshow(sobel_8u, cmap='gray')
    plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

    plt.show()

gradients()
# gradients2()