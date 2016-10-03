# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../../img/opencv.png')
# print img.shape, img.size, img.dtype

# BLUE = [255,0,0]
#
# img1 = cv2.imread('../../img/opencv.png')


#replicate
# replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
# constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
#
# plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
# plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
# plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

#split
base = np.zeros(img.shape, np.uint8)

channelBlue = np.zeros(img.shape, np.uint8)
channelGreen = np.zeros(img.shape, np.uint8)
channelRed = np.zeros(img.shape, np.uint8)

b,g,r = cv2.split(img)

channelBlue[:,:,0] = channelBlue[:,:,0] + b
channelGreen[:,:,1] = base[:,:,1] + g
channelRed[:,:,2] = base[:,:,2] + r

plt.subplot(151),plt.imshow(img),plt.title('SOURCE'),plt.xticks([]),plt.yticks([])
plt.subplot(152),plt.imshow(base),plt.title('BASE'),plt.xticks([]),plt.yticks([])
plt.subplot(153),plt.imshow(channelBlue),plt.title('BLUE'),plt.xticks([]),plt.yticks([])
plt.subplot(154),plt.imshow(channelGreen),plt.title('GREEN'),plt.xticks([]),plt.yticks([])
plt.subplot(155),plt.imshow(channelRed),plt.title('RED'),plt.xticks([]),plt.yticks([])

plt.show()
