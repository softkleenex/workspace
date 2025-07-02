# https://www.acmicpc.net/problem/30024

from sys import stdin
input = stdin.readline

import heapq

n, m = map(int, input().split())

place = [list(map(int, input().split())) for x in range(n)]
k  = int(input())



outheap = []


for y in range(0, n):
    for x in range(0, m):
        if y == 0 or y == n -1 or x == 0 or x == m - 1:
            heapq.heappush(outheap, (-place[y][x], y, x))

directions = [(-1 , 0), (+1 , 0), (0 , -1) , (0 , + 1)]

def outline(k):
    for t in range(k):
        while True:
            negval, y, x = heapq.heappop(outheap)
            val = -negval
            #초기값
            #if val != 0:
            if (val) !=  (place[y][x]):
                print(val, place[y][x], y, x)

            if place[y][x] != 0:
                break

        print(y + 1, x + 1)
        place[y][x] = 0

        
        for dy, dx in directions:
            ny, nx = (y + dy,  x + dx)
            if  0 <= ny < n and 0<= nx < m:
                if place[ny][nx] != 0:
                    heapq.heappush(outheap, (-place[ny][nx], ny, nx))
        
    
       
        


    
outline(k)
           