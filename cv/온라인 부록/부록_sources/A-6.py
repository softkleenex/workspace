# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 08:25:30 2022

@author: isor
"""

import numpy as np

print('화씨', '     섭씨')

for fahrenheit in np.arange(-30,151,0.5):
    celsius=round(((fahrenheit-32.0)*5.0)/9.0,2)
    print(fahrenheit,'-->',celsius)