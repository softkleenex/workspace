# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 07:20:49 2022

@author: isor
"""

import numpy as np

class TemperatureConversion:
    def __init__(self,position):
        self.pos=position # 소수점 pos자리에서 반올림
        
    def fahrenheit_to_celsius(self,val): # 화씨->섭씨 변환
        return round(((val-32.0)*5.0)/9.0,self.pos)
    
    def fahrenheit_to_celsius_table(self,start=0.0,end=100.0,inc=0.5):
        res=['화씨     섭씨']
        for fahrenheit in np.arange(start,end,inc):
            celsius=self.fahrenheit_to_celsius(fahrenheit)
            res.append(str(fahrenheit)+'-->'+str(celsius))
        return res

    def celsius_to_fahrenheit(self,val): # 섭씨->화씨 변환
        return round((val*9.0)/5.0+32.0,self.pos)
    
    def celsius_to_fahrenheit_table(self,start=0.0,end=100.0,inc=0.5):
        res=['섭씨     화씨']
        for celsius in np.arange(start,end,inc):
            fahrenheit=self.celsius_to_fahrenheit(celsius)
            res.append(str(fahrenheit)+'-->'+str(celsius))
        return res  
            
t=TemperatureConversion(3) 
ttable=t.fahrenheit_to_celsius_table(0,10,0.5)
for element in ttable:
    print(element)

#print(*ttable,sep='\n')
