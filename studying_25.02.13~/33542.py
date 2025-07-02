# https://www.acmicpc.net/problem/33542
#https://upload.acmicpc.net/e1ff45f1-7437-4902-bdc3-f595968ead1a/

from sys import stdin
input = stdin.readline
from bisect import bisect_left

a, b = map(int, input().split())

n = int(input())
left = []
right = []

for i in range(n):
    l, r = map(int, input().split())
    left.append((l, i + 1))
    right.append((r, i + 1))

target = a - b + 1 #이거 이상!

pair = []

if target <= 0:#안맞춰도되면
    pair = [-1, -1, -target]
    print(pair[0], pair[1])
    exit()
    


for i, v in enumerate(left):
    nowpair = [left[i][1],   -1 , (left[i][0] + 0) - target]
    if nowpair[2] >= 0 and (len(pair) == 0 or nowpair[2] < pair[2]):
        pair = nowpair


for i, v in enumerate(right):
    nowpair = [-1, right[i][1], (right[i][0] + 0) - target]
    if nowpair[2] >= 0 and (len(pair) == 0 or nowpair[2] < pair[2]):
        pair = nowpair
    

#하나 안맞추기, 양손 안맞추기는 끝!

right.sort(key = lambda x : x[0])


for i, v in enumerate(left):
   need = (target - left[i][0] , -float('inf'))#이거 이상인거 인덱스를 찾아라!
   tidx = bisect_left(right, need)#right는 정렬되어있음 pair[2], 즉, left[i] + right - target 이 최소인(둘의 인덱스가 같은경우 제외) 경우를 구하면된다
   while tidx < len(right):#찾은 값이 유효하다면?
        if right[tidx][1] == left[i][1]:#과녁 같으면 다음꺼 탐색
            tidx = tidx + 1
            if tidx == len(right):
                break 
            else:
                continue

        nowpair = [left[i][1], right[tidx][1], left[i][0] + right[tidx][0] - target]
        if len(pair) == 0 or (pair[2] > nowpair[2] and nowpair[2] >= 0):
            pair = nowpair
        break


if len(pair) == 0:
    print('No')
else:
    print(pair[0], pair[1])