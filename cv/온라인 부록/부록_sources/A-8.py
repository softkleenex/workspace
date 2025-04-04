# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 09:52:24 2022

@author: isor
"""

import numpy as np
    
def fahrenheit_to_celsius(val,pos): # 화씨->섭씨 변환(pos자리에서 반올림)
    result=round(((val-32.0)*5.0)/9.0,pos)
    return result

print('화씨', '     섭씨')

for fahrenheit in np.arange(-30,151,0.5):
    celsius=fahrenheit_to_celsius(fahrenheit,3)
    print(fahrenheit,'-->',celsius)