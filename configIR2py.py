# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 20:55:07 2019

@author: neo
"""

import serial
aquire  = [0xA5,0x35,0x01,0xDB]
baudrate= [0xA5,0x15,0x02,0xBC]
save = [0xA5,0x65,0x01,0x0b]
temp = bytes(aquire)
with serial.Serial('COM7', 19200, timeout=None) as ser:
    ser.write(bytes(baudrate))
    ser.write(temp)
    ser.write(bytes(save))
    s = ser.read(10000)
    data = s.hex()
    print(data)
    ser.close()