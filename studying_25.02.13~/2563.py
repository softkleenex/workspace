# https://www.acmicpc.net/problem/2563

n = int(input())
papers = [[0 for _ in range(101)] for _ in range(101)]

#첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다.
for t in range(n):
    x, y = (map(int, input().split()))
    papers[x][y] += 1
    papers[x + 10][y] -= 1
    papers[x][y + 10] -= 1
    papers[x + 10][y + 10] += 1




#x누적합
now = 0
for row in range(101):
    now = 0
    for col in range(1, 101):
        now += papers[row][col]
        papers[row][col] = now


#y누적합
now = 0
for col in range(101):
    now = 0
    for row in range(1, 101):
        now += papers[row][col]
        papers[row][col] = now


ans = 0
for row in range(100):
    for col in range(100):
        if papers[row][col] > 0:
            ans += 1


print(ans)