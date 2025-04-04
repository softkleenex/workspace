# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 09:42:07 2022

@author: isor
"""

import numpy as np
    
def fahrenheit_to_celsius(val): # 화씨->섭씨 변환(소수점 2자리에서 반올림)
    result=round(((val-32.0)*5.0)/9.0,2)
    return result

print('화씨', '     섭씨')

for fahrenheit in np.arange(-30,151,0.5):
    celsius=fahrenheit_to_celsius(fahrenheit)
    print(fahrenheit,'-->',celsius)