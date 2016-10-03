# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

cv2.LINE_AA = cv2.CV_AA

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print events

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),10,(255,0,0),-1,lineType=cv2.LINE_AA)


drawing = False # true if mouse is pressed
def draw_mousemove(event,x,y,flags,param):
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img, (x, y), (x, y), color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_mousemove)

while(1):
    cv2.imshow('image',img)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()