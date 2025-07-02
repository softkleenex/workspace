# https://www.acmicpc.net/problem/2805

# https://www.acmicpc.net/board/view/159942
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

trees = tuple(map(int, input().split()))




l = 0
r = 1000000000

ans = 0

while l <= r:
    mid = (l + r) // 2


    gettree = sum([x - mid for x in trees if x >= mid])#높이, 가져가는 나무
   

    if gettree >= m: #나무가 충분하다면
        ans = max(ans, mid)
        l = mid + 1#높이를 높여라!
        
    elif gettree < m:#나무가 부족하다면
        r = mid - 1#높이를 낮춰라!

        


print(ans)
    