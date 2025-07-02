# https://www.acmicpc.net/problem/15821

from sys import stdin
input = stdin.readline

from bisect import bisect_left


n, k = map(int, input().split())

# 첫 줄에는 낚시터를 나타내는 도형의 꼭짓점 수를 나타내는 자연수 Pi가 입력으로 주어진다.
# 두 번째 줄에는 해당 낚시터의 꼭짓점들의 좌표가 공백으로 구분되어 주어지며, 각 좌표는 x y형식으로 주어진다. 모든 좌표는 첫 번째 점을 기준으로 시계방향 혹은 반시계방향으로 주어진다. 모든 좌표는 정수이다.
# 각 낚시터가 서로 겹치는 경우는 없으며, 각 낚시터는 항상 넓이가 0보다 큰 다각형이며 서로 교차하지 않는다.

distances = []



for x in range(n):
    pi = int(input())
   
    space = tuple(map(int, input().split()))
    
    dis = pow((space[0] - 0), 2) + pow((space[1] - 0), 2)#초기값


    for x1, y1 in zip(space[::2], space[1::2]):
        dis = max(pow((x1 - 0), 2) + pow((y1 - 0), 2),   dis)


    distances.append(dis)
    
distances.sort()


print(float(distances[k-1]), '0', sep = '')