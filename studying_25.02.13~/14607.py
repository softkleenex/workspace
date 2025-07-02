# https://www.acmicpc.net/problem/14607




n = int(input())
ans = 0

joy = [0, 0, 2, 3, 6, 10]

if n <= 5:
    ans = (n, joy[n])
else:
    pre = (5, 10)
    for i in range(6 , n + 1):
        pre = (i, (i - 1) * 1 + pre[1])

    ans = pre





print(ans[1])