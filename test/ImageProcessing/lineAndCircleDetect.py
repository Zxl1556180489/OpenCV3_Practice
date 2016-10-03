# -*- coding: utf-8 -*-
import numpy as np
import cv2
import cv2.cv as cv
from matplotlib import pyplot as plt

def lineDtect():
    img = cv2.imread('../../img/sudoku.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 20, 70, apertureSize=3)

    # First parameter, Input image should be a binary image, so apply threshold or use canny edge detection before finding applying hough transform.
    # Second and third parameters are \rho and \theta accuracies respectively.
    # Fourth argument is the threshold, which means minimum vote it should get for it to be considered as a line.
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    # print lines
    # print '-----------'
    # print lines[:,0,:]
    for rho, theta in lines[0]:
    # for rho, theta in lines[:,0,:]:  for opencv3
        print '------------'
        print rho, theta
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # cv2.imwrite('houghlines3.jpg', img)
    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def lineDetectWithP():
    img = cv2.imread('../../img/sudoku.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 20, 70, apertureSize=3)
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    for x1, y1, x2, y2 in lines[0]:
        # for rho, theta in lines[:,0,:]:  for opencv3
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


cv2.HOUGH_GRADIENT = cv.CV_HOUGH_GRADIENT
def circleDetect():
    img = cv2.imread('../../img/circles.jpg', 0)
    img = cv2.medianBlur(img, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=50, param2=50, minRadius=0, maxRadius=0)

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 3)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow('detected circles', cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# lineDtect()
# lineDetectWithP()
circleDetect()