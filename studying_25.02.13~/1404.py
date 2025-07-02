# https://www.acmicpc.net/problem/1404

from decimal import Decimal


percent = list(map(int, input().split()))


winp = {(x): [] for x in range(0, 8)}



now = 0

for now in winp.keys():
    winp[now] = percent[now : now + (8 - now)]
    now += (8 - now)

print(winp, sep = '\n')