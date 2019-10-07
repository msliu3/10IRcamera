# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:23:09 2019

@author: neo
"""

import numpy as np
import cv2 as cv

img = cv.imread('enlarge-original.jpg',0)
img2 = cv.imread('enlarge-original.jpg',1)

ret,thresh = cv.threshold(img,106,255,0)
print(ret)
contours,hierarchy = cv.findContours(thresh,1,2)


cnt = contours[0]
M = cv.moments(cnt)
print(M,len(contours))

area = cv.contourArea(cnt)
print(area)
epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)

# =============================================================================
# x,y,w,h = cv.boundingRect(cnt)
# cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
# =============================================================================

# =============================================================================
# x,y,w,h = cv.boundingRect(contours[1])
# cv.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
# =============================================================================

hull = cv.convexHull(contours[0])
foot = []
for a in hull:
    if a[0][1]>100:
        foot.append(a)
print(foot)

rect = cv.minAreaRect(np.array(foot))
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img2,[box],0,(0,0,255),2)

cv.drawContours(img2,foot,-1,(255,0,0),3)
x,y,w,h = cv.boundingRect(np.array(foot))
cv.rectangle(img2,(x,y),(x+w,y+h),(0,0,255),2)

hull = cv.convexHull(contours[1])
foot = []
for a in hull:
    if a[0][1]>100:
        foot.append(a)
print(foot)

rect = cv.minAreaRect(np.array(foot))
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img2,[box],0,(0,0,255),2)

cv.drawContours(img2,foot,-1,(255,0,0),3)
x,y,w,h = cv.boundingRect(np.array(foot))
cv.rectangle(img2,(x,y),(x+w,y+h),(0,0,255),2)

cv.drawContours(img,contours,-1,(0,0,255),2)

cv.imshow("hehe",img)
cv.waitKey(0)
cv.destroyAllWindows()