# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

def detectFace(img):
    cascade = cv2.CascadeClassifier(
        'E:\\OpenCV\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt.xml')

    face = cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=3, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)

    if len(face) == 0:
        return []
    face[:, 2:] +=face[:, :2]
    return face

def drawRects(img, rects):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1 * 2, y1 * 2), (x2 * 2, y2 * 2), (255,0,0), 2)        #放大矩形框，在原图上显示


def captureVideo():
    cap = cv2.VideoCapture(0)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (320, 240))         #缩小分辨率，加快处理速度

        # 翻转图像，flipCode：1：水平翻转；0：垂直翻转；-1：水平垂直翻转
        gray = cv2.flip(gray,flipCode=1)
        frame = cv2.flip(frame,flipCode=1)

        drawRects(frame, detectFace(gray))

        # Display the resulting frame
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)

        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord('s'):
            cv2.imwrite('../../img/save.png', frame)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

captureVideo()