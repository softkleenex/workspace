# https://www.acmicpc.net/problem/2910
from collections import Counter




n, c = map(int, input().split())

x = list(input().split())

counterx = Counter(x)


counterx = counterx.items()

counterx = sorted(counterx, key = lambda x : -x[1])


for x in counterx:
    for _ in range(x[1]):
        print(x[0], end = ' ')