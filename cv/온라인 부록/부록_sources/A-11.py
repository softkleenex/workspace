# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 11:24:41 2022

@author: isor
"""

import numpy as np
    
def fahrenheit_to_celsius(val,pos=1): # 화씨->섭씨 변환(pos자리에서 반올림, 기본은 1자리)
    return round(((val-32.0)*5.0)/9.0,pos)

def fahrenheit_to_celsius_table(start=0.0,end=100.0,inc=0.5): # 온도 변환 표 작성
    print('화씨', '     섭씨')
    for fahrenheit in np.arange(start,end,inc):
        print(fahrenheit,'-->',fahrenheit_to_celsius(fahrenheit))
        
fahrenheit_to_celsius_table()
