# https://www.acmicpc.net/problem/10953

t = int(input())

for x in range(t):
    a, b = map(int, input().split(','))
    print(a + b)