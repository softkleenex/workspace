# https://www.acmicpc.net/problem/16567

from sys import stdin
from collections import deque
input = stdin.readline

from bisect import bisect_left

n, m = map(int, input().split())

road = list(map(int, input().split()))




tesk = deque()

for _ in range(m):
    temp = list(map(int, input().split()))
    tesk.append(temp) 



ans = 0

for i, v in enumerate(road):
   
        if v == 1 and  (i == 0 or road[i - 1] == 0):
            ans += 1





while tesk:
    now = tesk.popleft()
    if now[0] == 1:#더럽히는 시련이라면
        nowidx = now[1] - 1
       # 새롭게 더럽혀지는 경우만 갱신
        if road[nowidx] == 0:
            road[nowidx] = 1

            left = nowidx - 1
            left_clean = 0 <= left and road[left] == 0
            left_dirty = 0 <= left and road[left] == 1
            
            right = nowidx + 1
            right_clean  = right < n and road[right] == 0
            right_dirty = right < n and road[right] == 1

            if left_dirty and right_dirty:#둘다 더러움
                 ans -= 1
            elif left_clean and right_clean:#둘다 꺠끗함
                 ans += 1
            elif (left_clean and not right_dirty) or (not left_dirty and right_clean):
                ans += 1

            


        
    elif now[0] == 0:
        print(ans)
    else:
        print('error')