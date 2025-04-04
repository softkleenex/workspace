# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 14:48:57 2022

@author: isor
"""

import numpy as np

class TemperatureConversion:
    def fahrenheit_to_celsius(self,val,pos=1): # 화씨->섭씨 변환(pos자리에서 반올림, 기본은 1자리)
        return round(((val-32.0)*5.0)/9.0,pos)
    
    def fahrenheit_to_celsius_table(self,start=0.0,end=100.0,inc=0.5): # 온도 변환 표 작성
        print('화씨', '     섭씨')
        for fahrenheit in np.arange(start,end,inc):
            celsius=self.fahrenheit_to_celsius(fahrenheit)
            print(fahrenheit,'-->',celsius)

    def celsius_to_fahrenheit(self,val,pos=1): # 화씨->섭씨 변환(pos자리에서 반올림, 기본은 1자리)
        return round((val*9.0)/5.0+32.0,pos)
    
    def celsius_to_fahrenheit_table(self,start=0.0,end=100.0,inc=0.5):
        print('섭씨', '     화씨')
        for celsius in np.arange(start,end,inc):
            fahrenheit=self.celsius_to_fahrenheit(celsius)
            print(celsius,'-->',fahrenheit)    
            
t=TemperatureConversion()

t.fahrenheit_to_celsius_table() # 화씨->섭씨 변환 표 출력
print('\n섭씨 0도=화씨 ',t.celsius_to_fahrenheit(0.0)) # 섭씨 0.0도에 해당하는 화씨 출력