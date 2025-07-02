# https://www.acmicpc.net/problem/2072


n = 25

b = set()
w = set()

ans = -1

def end(t):
    return True


for x in range(1, n + 1):
    temp = (map(int, input().split()))
    if x % 2 == 0:
        b.add((temp))
    else:
        w.add((temp))

    if ans == -1:
        ans = x

print(ans)