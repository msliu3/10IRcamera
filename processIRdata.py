# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:01:47 2019

#图像处理部分测试结果
1.先从工具端截取一帧的画面
2.同时保留一帧的画面数据
3.通过数据还原出图像，在加模糊滤镜
4.和照片进行比对


5A5A0206针头

32x24 = 768

针头 2
器件温度 1
验证     1

768 + 4 = 772



@author: neo
"""
import numpy as np
from PIL import Image,ImageFilter
f = open('./05foot.txt', 'r')
pic = f.read()
#print(pic)
frame = []
#两个字节为一组
for i in range(int(len(pic)/4)):
    frame.append(pic[i*4:i*4+4])
    
#list[string,string,string......]
temp = []
for i in range(2,771):
    t = (int(frame[i][2:4],16)*256 + int(frame[i][0:2],16))/100
    temp.append(t)

env = temp.pop()

temperature = []
for i in temp:
    temperature.append(int(i))

for i in range(24):
    for j in range(32):
        print('%2d'%temperature[j + i*32],end=" ")
    print()

maxtemp = max(temp)
mintemp = min(temp)

for i in range(len(temp)):
        temp[i] = int((temp[i]-mintemp)/(maxtemp-mintemp)*255)
#print(temp)

# =============================================================================
# newtemp = []
# for y in range(24):
#     for x in range(32):
#         newtemp.append(temp[31 - x + y*32])
# data = np.array(newtemp).reshape(24,32)
# =============================================================================

data = np.array(temp).reshape(24,32)
#print(data)
temperature = np.array(temperature,np.float32).reshape(24,32)

#rgbdata = np.array([data,temperature,data],np.uint8).reshape(3,-1)
rgbdata = np.array([data,data,data],np.uint8).reshape(3,-1)

rgbdata = rgbdata.T.reshape(24,32,3)


image2 = Image.fromarray(rgbdata)
image2.save("./original.jpg")
im = image2.filter(ImageFilter.SMOOTH_MORE)
#image2.show()
image2 = image2.resize((320,240))
#im = Image.open("./testpic.jpg")
image2.show()
#im = im.resize((320,240))
im.show()
array = np.array(im)          # array is a numpy array 
#image2 = Image.fromarray(array)  
image2.save("./output.jpg")
im.save("./output2.jpg")