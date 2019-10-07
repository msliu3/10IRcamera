ai# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:39:40 2019

#用python写一个程序读取红外摄像头的数据，并加入模糊滤镜

@author: neo
"""
import serial


headSize = 4
def checkHeaddata(data=[]):
    global headSize 
    if len(data)!= headSize:
        print('The length of head is not equal to 4')
        return False
    
#    This is head data from one frame
    head = [0x5A,0x5A,0x02,0x06]
#    head = [0x5A,0x5A]
    for i in range(headSize):
        if data[i] != head[i]:
#            print(data)
            return False
    return True
    
head = []
data = []
string = ''
with serial.Serial('COM7', 115200, timeout=None) as ser:
    while True:
        s = ser.read(1).hex()
        string = string + s
        if s != "":
            s = int(s,16)
#        s = int((ser.read()).hex(),16)
        head.append(s)
#        print(head)
        if len(head) == headSize:
            if checkHeaddata(head):
                temp = ser.read(1540)
                data.append(temp.hex())
            
            head.pop(0)
#            print(True)
        if len(data) == 5:
            print(data[4])
            break
ser.close()

