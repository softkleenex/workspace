# https://www.acmicpc.net/problem/11578


from itertools import combinations
import collections
from sys import stdin


input = stdin.readline

n, m = map(int, input().split())
#문제의수, 고를수있는 팀원 개수

mem = list()


for x in range(m):
    temp = (tuple(map(int, input().split()))[1:])
    mem.append(temp)

mem = tuple(mem)


for x in range(0, m + 1):
    now = combinations(mem, x)
    for x2 in now:
        # print(x2)
        now2 = set().union(*x2)
        if len(now2) == n:
            print(x)
            exit()



print(-1)