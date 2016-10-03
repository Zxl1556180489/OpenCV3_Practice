# -*- coding: utf-8 -*-
import cv2
import numpy as np
import random

cv2.LINE_AA = cv2.CV_AA

img = np.zeros((512,512,3), np.uint8)

for i in range(81):
    x = random.randrange(10,500,1)
    y = random.randrange(10,500,1)
    radius = int(random.gauss(18,8))
    if radius < 0:
        radius = 0
    blue = random.randrange(110,255,1)
    green = random.randrange(110,255,1)
    red = random.randrange(150,255,1)
    cv2.circle(img, (x, y), radius, (blue, green, red), -1, lineType=cv2.LINE_AA)

cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey (0)
cv2.destroyAllWindows()