# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 09:29:28 2022

@author: isor
"""

print('화씨', '     섭씨')

for fahrenheit in range(-30,151,1):
    celsius=round(((fahrenheit-32.0)*5.0)/9.0,2)
    print(fahrenheit,'-->',celsius)