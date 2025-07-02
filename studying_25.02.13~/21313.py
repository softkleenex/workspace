# https://www.acmicpc.net/problem/21313

n = int(input())

ans = []

for i in range(n):
    if i % 2 == 0:
        ans.append(1)
    else:
        ans.append(2)

while ans [-2] == ans[-1]or ans[0] == ans[-1]:
    ans[-1] += 1

print(*ans, sep = ' ')