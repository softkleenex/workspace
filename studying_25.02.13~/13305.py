# https://www.acmicpc.net/problem/13305
from sys import stdin
input = stdin.readline

n = int(input())

#도시의 거리
roads = tuple(map(int, input().split()))

#각 도시에 배정된 리터당 기름의 가격
costs = tuple(map(int, input().split()))
costs = costs[:-1]

target = tuple(zip(roads, costs))

nowcost = target[0][1]#가장 첫 road의 가격
ans = 0

for x in target:
    needlenght = x[0]#가야하는 길이
    nowcost = min(nowcost, x[1])
    ans += nowcost * needlenght


print(ans)