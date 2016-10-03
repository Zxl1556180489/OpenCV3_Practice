# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import displayUtil

# OpenCV has the function cv2.cornerHarris() for this purpose. Its arguments are :
#
# img - Input image, it should be grayscale and float32 type.
# blockSize - It is the size of neighbourhood considered for corner detection
# ksize - Aperture parameter of Sobel derivative used.
# k - Harris detector free parameter in the equation.

img = cv2.imread('../../img/blox.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def Harris(img, gray):
    newImg = img.copy()
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)

    # result is dilated for marking the corners, not important
    dst = cv2.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image.
    newImg[dst > 0.01 * dst.max()] = [0, 0, 255]

    return (newImg, 'Harris')


def ShiTomasi(img, gray):
    newImg = img.copy()
    corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(newImg, (x, y), 3, 255, -1)

    return (newImg, 'Shi-Tomasi')


def SIFT(gray):
    # sift = cv2.SIFT()
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(gray, None)

    img = None
    img = cv2.drawKeypoints(gray, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    return (img, 'SIFT')


def SURF(gray):
    # surf = cv2.SURF(500)
    surf = cv2.xfeatures2d.SURF_create(500)
    kp = surf.detect(gray, None)
    img = cv2.drawKeypoints(gray, kp, None, (255, 0, 0), 4)
    return (img, 'SURF')


def FAST(img):
    # Initiate FAST object with default values
    # fast = cv2.FastFeatureDetector()

    # use this for OpenCV3.0
    fast = cv2.FastFeatureDetector_create()

    # find and draw the keypoints
    kp = fast.detect(img, None)
    img2 = None
    img2 = cv2.drawKeypoints(img, kp, img2, color=(255, 0, 0))

    # Print all default params
    # print "Threshold: ", fast.getInt('threshold')
    # print "nonmaxSuppression: ", fast.getBool('nonmaxSuppression')
    # print "Total Keypoints with nonmaxSuppression: ", len(kp)

    return (img2, 'FAST')


def ORB(img):
    orb = cv2.ORB_create()

    # find the keypoints with ORB
    kp = orb.detect(img, None)

    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)

    # draw only keypoints location,not size and orientation
    img2 = None
    img2 = cv2.drawKeypoints(img, kp, img2, color=(0, 255, 0), flags=0)

    return (img2, 'ORB')


displayUtil.showImgWithPLT((Harris(img, gray), ShiTomasi(img, gray), SIFT(gray), SURF(gray), FAST(img), ORB(img)))
