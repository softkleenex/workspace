# https://www.acmicpc.net/problem/31738
import math


n, m = map(int, input().split())



if n >= m:
    print(0)
else:
    a = 1
    for x in range(1, n + 1):
        a = (a * x) % m
    print(a)