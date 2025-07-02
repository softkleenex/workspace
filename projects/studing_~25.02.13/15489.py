# https://www.acmicpc.net/problem/15489
from sys import stdin
input = stdin.readline

r, c, w = map(int, input().split())


#r, c에서 출발해서, w만큼을 내려가야 한다

triangle = [[1]]

for x in range(1, r + w -1):
    temp = [1]
    for x2 in range(1, x):
        temp.append(triangle[x - 1][x2-1] + triangle[x - 1][x2] )
    temp.append(1)
    triangle.append(temp)

# print(*triangle, sep = '\n')



ans = 0

start = [r-1, c-1]



for x in range(w):


    for x2 in range(0, x+1):
        
        # print(start[0], start[1] + x2, triangle[start[0]][ start[1] + x2])
        ans += triangle[start[0]][ start[1] + x2]

    start[0] += 1

print(ans)