# https://www.acmicpc.net/problem/16922

import itertools
import sys

input = sys.stdin.readline

n = int(input())

target = [1, 5, 10, 50]
#4개중에 중복허용해서 n개 고르는 개수

# print(help(itertools.combinations))

ans = [sum(x) for x in list((itertools.combinations_with_replacement(target, n)))]
print(len(set(ans)))
