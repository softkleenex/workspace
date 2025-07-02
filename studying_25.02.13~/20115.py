# https://www.acmicpc.net/problem/20115

from sys import stdin
import heapq

n = map(int, (input().split()))



drinks = list(map(float, input().split()))

max_d = max(drinks)
drinks.remove(max_d)
other_d = sorted(drinks)


for x in other_d:
    max_d += (x) / 2

print(max_d)