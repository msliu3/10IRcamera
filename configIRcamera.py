# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:39:40 2019

#用python写一个程序读取红外摄像头的数据，并加入模糊滤镜

@author: neo
"""
import serial
with serial.Serial('COM7', 19200, timeout=1) as ser:
    x = ser.read()          # read one byte
    s = ser.read(10)        # read up to ten bytes (timeout)
    line = ser.readline()   # read a '\n' terminated line

