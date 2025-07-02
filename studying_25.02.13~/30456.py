# https://www.acmicpc.net/problem/30456

n, l = map(int, input().split())

print(*([1] * (l- 1)), n, sep = '')