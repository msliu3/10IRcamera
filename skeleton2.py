# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 01:03:10 2019

@author: neo
"""

from skimage import morphology,data,color
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('./enlarge-original.jpg',0)
ret,thresh1=cv2.threshold(img,100,1,cv2.THRESH_BINARY)
plt.imshow(thresh1,'gray')  
plt.title("THRESH_BINARY")  
plt.xticks([]),plt.yticks([])
plt.show()  

image=color.rgb2gray(data.horse())
image=1-image #反相

skeleton =morphology.skeletonize(thresh1)#thresh1
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
ax1.imshow(thresh1, cmap=plt.cm.gray)#img
ax1.axis('off')
ax1.set_title('original', fontsize=20)
ax2.imshow(skeleton, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('skeleton', fontsize=20)
fig.tight_layout()
plt.show()
