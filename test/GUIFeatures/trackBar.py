# -*- coding: utf-8 -*-
import cv2
import numpy as np

cv2.LINE_AA = cv2.CV_AA

def nothing(x):
    pass

def draw_circle(event,x,y,flags,param):
    global blue, green, red, r
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),r,(blue,green,red),-1,lineType=cv2.LINE_AA)

# Create a black image, a window and bind the function to window
img = np.zeros((400,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

# create trackbars for color change
cv2.createTrackbar('R','image', 0, 255, nothing)
cv2.createTrackbar('G','image', 0, 255, nothing)
cv2.createTrackbar('B','image', 0, 255, nothing)
cv2.createTrackbar('r','image', 0, 100, nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

# blue = 0
# green = 0
# red = 0

while(1):
    cv2.imshow('image',img)
    key = cv2.waitKey(1)

    if key & 0xFF == ord('q'):
        break

    # get current positions of four trackbars
    red = cv2.getTrackbarPos('R','image')
    green = cv2.getTrackbarPos('G','image')
    blue = cv2.getTrackbarPos('B','image')
    r = cv2.getTrackbarPos('r','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        # img[:] = [b,g,r]
        pass

cv2.destroyAllWindows()