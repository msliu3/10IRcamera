# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:12:21 2019

@author: neo
"""

import serial
aquire  = [0xA5,0x35,0x01,0xDB]
with serial.Serial('COM7', 115200, timeout=None) as ser:
    ser.write(bytes(aquire))
    while True:
        s = ser.read(1)
        data = s.hex()
        print(data)
    ser.close()