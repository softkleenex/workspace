# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 09:59:00 2022

@author: isor
"""

import numpy as np
    
def fahrenheit_to_celsius(val,pos): # 화씨->섭씨 변환(pos자리에서 반올림)
    return round(((val-32.0)*5.0)/9.0,pos)

print('화씨', '     섭씨')

for fahrenheit in np.arange(-30,151,0.5):
    print(fahrenheit,'-->',fahrenheit_to_celsius(fahrenheit,3))