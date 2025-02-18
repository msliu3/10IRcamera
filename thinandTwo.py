# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 00:03:41 2019

@author: neo
"""
import cv2
 
#细化函数，输入需要细化的图片（经过二值化处理的图片）和映射矩阵array
#这个函数将根据算法，运算出中心点的对应值
def Thin(image,array):
    h,w = image.shape
    iThin = image
 
    for i in range(h):
        for j in range(w):
            if image[i,j] == 0:
                a = [1]*9
                for k in range(3):
                    for l in range(3):
                        #如果3*3矩阵的点不在边界且这些值为零，也就是黑色的点
                        if -1<(i-1+k)<h and -1<(j-1+l)<w and iThin[i-1+k,j-1+l]==0:
                            a[k*3+l] = 0
                sum = a[0]*1+a[1]*2+a[2]*4+a[3]*8+a[5]*16+a[6]*32+a[7]*64+a[8]*128
                #然后根据array表，对ithin的那一点进行赋值。
                iThin[i,j] = array[sum]*255
    return iThin        
    
#最简单的二值化函数，阈值根据图片的昏暗程度自己设定，我选的180
def Two(image):
    w,h = image.shape
    size = (w,h)
    iTwo = image
    for i in range(w):
        for j in range(h):
            if image[i,j]<180:
                iTwo[i,j] = 0 
            else:
                iTwo[i,j] = 255
    return iTwo
 
#映射表
array = [0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,\
         1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,\
         0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,\
         1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,\
         1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,\
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
         1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,\
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
         0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,\
         1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,\
         0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,\
         1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,\
         1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,\
         1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,\
         1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,0,\
         1,1,0,0,1,1,1,0,1,1,0,0,1,0,0,0]
 
#读取灰度图片，并显示
img = cv2.imread('./enlarge-original.jpg',0) #直接读为灰度图像
cv2.imshow('image',img)
#cv2.waitKey(0)
 
#自适应二值化函数，需要修改的是55那个位置的数字，越小越精细，细节越好，噪点更多，最大不超过图片大小
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,55,2) #换行符号 \
cv2.imshow('iTwo',th3)
#cv2.waitKey(0)
 
#获取自适应二值化的细化图，并显示
iThin = Thin(th3,array)
cv2.imshow('iThin',iThin)
#cv2.waitKey(0)
 
#获取简单二值化的细化图，并显示
iTwo = Two(img)
iThin_2 = Thin(iTwo,array)
cv2.imshow('iTwo_2',iThin_2)
cv2.waitKey(0)
 
#cv2.destroyAllWindows()