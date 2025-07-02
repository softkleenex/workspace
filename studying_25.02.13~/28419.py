# https://www.acmicpc.net/problem/28419

n = int(input())
list1 = list(map(int, input().split()))

a = 0
for x in range(0, len(list1) + 1, 2):
    if x < len(list1):
        a += list1[x]


b = 0
for x in range(1, len(list1) + 1, 2):
    if x < len(list1):
        b += list1[x]

if n == 3 and a > b:
    print(-1)
else:
    print(abs(a - b))