# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:27:49 2019

@author: neo
"""

import cv2
 
img = cv2.imread('./testpic.jpg',cv2.IMREAD_UNCHANGED)
cv2.imshow('image',img)