# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImg(fileName=''):
    img = cv2.imread(fileName)
    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    cv2.waitKey (0)
    cv2.destroyAllWindows()

def showImgWithPLT(fileName=''):
    img = cv2.imread(fileName)
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

def captureVideo():
    cap = cv2.VideoCapture(0)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 翻转图像，flipCode：1：水平翻转；0：垂直翻转；-1：水平垂直翻转
        gray = cv2.flip(frame,flipCode=1)

        # gray = salt(gray,500)

        # Display the resulting frame
        cv2.imshow('frame', gray)
        key = cv2.waitKey(1)

        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord('s'):
            cv2.imwrite('../../img/save.png', gray)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j,i] = 255
        elif img.ndim == 3:
            img[j,i,0]= 255
            img[j,i,1]= 255
            img[j,i,2]= 255
    return img

# showImgWithPLT('../../img/loading.jpg')
captureVideo()