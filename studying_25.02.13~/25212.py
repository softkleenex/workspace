# https://www.acmicpc.net/problem/25212

from sys import stdin
from itertools import combinations
from decimal import Decimal

n = int(input())

cakes = list(Decimal(1)  / Decimal(x) for x in list(map(int, input().split())))

case = 0

for x in range(1, n + 1):
    nowcakes = tuple(cake for cake in combinations(cakes, x) if Decimal('0.99000') <= sum(cake) <= Decimal('1.01000'))
    case += len(nowcakes)


print(case)

