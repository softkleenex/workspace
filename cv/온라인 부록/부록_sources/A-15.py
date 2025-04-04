# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 15:28:15 2022

@author: isor
"""

import numpy as np

class TemperatureConversion:
    def __init__(self,position):
        self.pos=position # 소수점 pos자리에서 반올림
        
    def fahrenheit_to_celsius(self,val): # 화씨->섭씨 변환
        return round(((val-32.0)*5.0)/9.0,self.pos)
    
    def fahrenheit_to_celsius_table(self,start=0.0,end=100.0,inc=0.5):
        print('화씨', '     섭씨')
        for fahrenheit in np.arange(start,end,inc):
            celsius=self.fahrenheit_to_celsius(fahrenheit)
            print(fahrenheit,'-->',celsius)

    def celsius_to_fahrenheit(self,val): # 섭씨->화씨 변환
        return round((val*9.0)/5.0+32.0,self.pos)
    
    def celsius_to_fahrenheit_table(self,start=0.0,end=100.0,inc=0.5):
        print('섭씨', '     화씨')
        for celsius in np.arange(start,end,inc):
            fahrenheit=self.celsius_to_fahrenheit(celsius)
            print(celsius,'-->',fahrenheit)    
            
t1=TemperatureConversion(3) # 셋쨰 자리에서 반올림하는 객체
t2=TemperatureConversion(1) # 첫째 자리에서 반올림하는 객체

t1.fahrenheit_to_celsius_table(0,10,0.5)
t2.fahrenheit_to_celsius_table(0,10,0.5)

print('\n섭씨 -0.21도=화씨 ',t1.celsius_to_fahrenheit(-0.21),'(셋째 자리 반올림)')
print('\n섭씨 -0.21도=화씨 ',t2.celsius_to_fahrenheit(-0.21),'(첫째 자리 반올림)')