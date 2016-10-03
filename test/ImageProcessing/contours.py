# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImg(img):
    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def contours():
    im = cv2.imread('../../img/box.png')
    im = cv2.medianBlur(im, 5)

    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2.5)

    # derp, contours, hierarchy = cv2.finContours() for opencv3
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cnt = contours[4]
    # cv2.drawContours(im, [cnt], -1, (0, 255, 0), 3)
    cv2.drawContours(im, contours, -1, (0, 255, 0), 3)

    cnt = contours[0]
    M = cv2.moments(cnt)
    print M

    showImg(im)

def contourFeatures():
    im = cv2.imread('../../img/flash.png')
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2.5)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[2]
    approximation = im.copy()
    imHull = im.copy()
    rectangle = im.copy()
    circle = im.copy()
    ellipse = im.copy()

    # Contour Approximation
    epsilon = 0.02 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    cv2.drawContours(approximation, [approx], -1, (0, 255, 0), 2)

    # Convex Hull
    hull = cv2.convexHull(cnt)
    cv2.drawContours(imHull, [hull], -1, (0, 255, 0), 3)

    # Straight Bounding Rectangle & Rotated Rectangle
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(rectangle, (x, y), (x + w, y + h), (0, 255, 0), 2)

    rect = cv2.minAreaRect(cnt)

    # use cv2.boxPoints(rect) for opencv3
    box = cv2.cv.BoxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(rectangle, [box], 0, (0, 0, 255), 2)

    # Minimum Enclosing Circle
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    radius = int(radius)
    cv2.circle(circle, center, radius, (0, 255, 0), 2)

    # Fitting an Ellipse
    e = cv2.fitEllipse(cnt)
    cv2.ellipse(ellipse, e, (0, 255, 0), 2)

    titles = ['Original Image', 'Approximation', 'Convex Hull', 'Rectangle', 'Enclosing Circle', 'Fit Ellipse']
    images = [im, approximation, imHull, rectangle, circle, ellipse]

    for i in xrange(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()

# contours()
contourFeatures()