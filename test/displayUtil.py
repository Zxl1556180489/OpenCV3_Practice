# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math


def showImgWithCV2(img):
    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def showImgWithPLT(imgTuple):
    n = len(imgTuple)
    if (n <= 3):
        for i in xrange(n):
            plt.subplot(1, n, i + 1)
            if (len(imgTuple[i]) == 2):
                plt.imshow(cv2.cvtColor(imgTuple[i][0], cv2.COLOR_BGR2RGB))
                plt.title(imgTuple[i][1])
            else:
                plt.imshow(cv2.cvtColor(imgTuple[i], cv2.COLOR_BGR2RGB))

            plt.xticks([]), plt.yticks([])
    else:
        for i in xrange(n):
            plt.subplot(2, math.ceil(float(n) / 2), i + 1)
            if (len(imgTuple[i]) == 2):
                plt.imshow(cv2.cvtColor(imgTuple[i][0], cv2.COLOR_BGR2RGB))
                plt.title(imgTuple[i][1])
            else:
                plt.imshow(cv2.cvtColor(imgTuple[i], cv2.COLOR_BGR2RGB))

            plt.xticks([]), plt.yticks([])

    plt.show()

# img1 = cv2.imread('./VideoAnalysis/a.jpg')
# img2 = cv2.imread('./VideoAnalysis/s.jpg')
# img3 = cv2.imread('./VideoAnalysis/d.jpg')
# showImgWithPLT(((img1,''),(img2,''),(img3,'')))