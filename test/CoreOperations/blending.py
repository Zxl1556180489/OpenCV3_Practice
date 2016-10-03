# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('../../img/circles.jpg')
img2 = cv2.imread('../../img/loading.jpg')

img1 = cv2.resize(img1,img2.shape[:2])

# print img1.shape, img2.shape[:2]

dst = cv2.addWeighted(img1,0.5,img2,1,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()