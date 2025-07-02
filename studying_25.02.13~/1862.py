# https://www.acmicpc.net/problem/1862

n = input()#9진수
ans = 0

for i, v in enumerate(n):
    nowv = int(v)
    if nowv >= 5:
        nowv -= 1

    temp = int(nowv) * pow(9, len(n) - i - 1)

    ans += temp


print(ans)
    