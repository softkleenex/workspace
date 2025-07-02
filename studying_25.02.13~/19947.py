# https://www.acmicpc.net/problem/19947

h, y = map(int, input().split())

money = [h for i in range(y + 1)]



for i in range(1, y+ 1):
    money[i] = int(money[i - 1] * 1.05)
    if i >= 3:
        money[i] = max(money[i], int(money[i - 3] * 1.2))
    if i >= 5:
        money[i] = max(money[i], int(money[i - 5] * 1.35))

print(money[-1])