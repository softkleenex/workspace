# https://www.acmicpc.net/problem/17086

from collections import deque

n, m = map(int, input().split())

space = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

dist = [[-1] * m for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if space[i][j] == 1:
            q.append((i, j))
            dist[i][j] = 0


while q:
    y, x = q.popleft()
    for d in range(8):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < n and 0 <= nx < m and dist[ny][nx] == -1:
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))


if max(map(max, dist)) != max(max(dist)):
    exit(1)

ans = max(map(max, dist))

print(ans)