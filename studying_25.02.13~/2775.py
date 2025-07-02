# https://www.acmicpc.net/problem/2775
from sys import stdin
input = stdin.readline

t = int(input())

#k층 n 호

home = [[x for x in range(1, 14 + 1)] for x2 in range(0, 14 + 1)]

for x in range(1, 14 + 1):
    for x2 in range(0, 14 ):
        home[x][x2] = sum(home[x - 1][:x2 +1])
    


# print(*home, sep = '\n')

for _ in range(t):
    k = int((input()))
    n = int(input())
    print(home[k][n - 1])

            