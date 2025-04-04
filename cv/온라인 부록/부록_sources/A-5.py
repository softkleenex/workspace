# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 07:44:30 2022

@author: isor
"""

print('화씨', '     섭씨')

fahrenheit=-30
while fahrenheit<=150:
    celsius=round(((fahrenheit-32.0)*5.0)/9.0,2)
    print(fahrenheit,'-->',celsius)
    fahrenheit=fahrenheit+1