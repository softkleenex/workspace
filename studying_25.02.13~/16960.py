# https://www.acmicpc.net/problem/16960

from sys import stdin
input = stdin.readline

from itertools import combinations

n, m = map(int, input().split())

sw = dict()

for x in range(n):
    temp = list(map(int, input().split()))
    sw[x] = tuple(temp[1:])


target = set(x for x in range(1, m+1))


for nowsw in combinations(sw.values(), n - 1):
    now = set()
    for x in nowsw:
        now.update(x)
    

    if now == target:
        print(1)
        exit()





print(0)
