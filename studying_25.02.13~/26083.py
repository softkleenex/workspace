# https://www.acmicpc.net/problem/26083

from datetime import datetime
from sys import stdin
input = stdin.readline


nowy, nowm, nowd = map(int, input().split()) 

today = tuple((nowy, nowm, nowd))

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    tries = ((a, b, c) , (c, b, a) , (c, a, b))
    
    validdates = []

    for x, y, z in tries:
        try:
            datetime(2000 + x, y, z)
            validdates.append(tuple((x, y, z)))
        except:
            continue
        
    
    if len(validdates) == 0:
        print('invalid')
    elif all(today <= x for x in validdates):
        print('safe')
    else:
        print('unsafe')
   