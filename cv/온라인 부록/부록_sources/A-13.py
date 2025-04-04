# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 14:17:23 2022

@author: isor
"""

import numpy as np

class TemperatureConversion:
    """
    온도를 변환하는 클래스
    멤버 함수 fahrenheit_to_celsius: 화씨를 섭씨로 변환
    멤버 함수 fahrenheit_to_celsius_table: 화씨를 섭씨로 변환하는 표 작성
    """
    
    def fahrenheit_to_celsius(self,val,pos=1): # 화씨->섭씨 변환(pos자리에서 반올림, 기본은 1자리)
        return round(((val-32.0)*5.0)/9.0,pos)
    
    def fahrenheit_to_celsius_table(self,start=0.0,end=100.0,inc=0.5): # 온도 변환 표 작성
        print('화씨', '     섭씨')
        for fahrenheit in np.arange(start,end,inc):
            celsius=self.fahrenheit_to_celsius(fahrenheit)
            print(fahrenheit,'-->',celsius)

t=TemperatureConversion()

t.fahrenheit_to_celsius_table()
print('\n화씨 100.0도=섭씨',t.fahrenheit_to_celsius(100.0,3))