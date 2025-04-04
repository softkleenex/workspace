# # 위 그림은 첫 번째 예제를 나타낸 것입니다. 나침반을 작동시키면 왼쪽 그림과 같이 붉은색 침이 상하좌우 대각선 8방향 중 보물의 방향을 가리킵니다.

# # 위쪽부터 시계방향으로 각각 1번부터 8번 방향으로 정의합니다. 각 방향에 대한 설명은 다음과 같습니다.

# # 좌표 $(x,y)$는 위에서부터 $x$번째 칸, 왼쪽에서부터 $y$번째 칸을 의미합니다. ($x, y$는 1이상 $N$이하의 양의 정수입니다.)

# # 1번 방향: 보물은 $x$좌표가 작고, $y$좌표가 같은 곳에 있습니다.
# # 2번 방향: 보물은 $x$좌표가 작고, $y$좌표가 큰 곳에 있습니다.
# # 3번 방향: 보물은 $x$좌표가 같고, $y$좌표가 큰 곳에 있습니다.
# # 4번 방향: 보물은 $x$좌표가 크고, $y$좌표가 큰 곳에 있습니다.
# # 5번 방향: 보물은 $x$좌표가 크고, $y$좌표가 같은 곳에 있습니다.
# # 6번 방향: 보물은 $x$좌표가 크고, $y$좌표가 작은 곳에 있습니다.
# # 7번 방향: 보물은 $x$좌표가 같고, $y$좌표가 작은 곳에 있습니다.
# # 8번 방향: 보물은 $x$좌표가 작고, $y$좌표가 작은 곳에 있습니다.
# #  $M$번의 나침반 사용기록을 이용해 보물의 위치를 찾아주세요. 나침반을 작동시킨 위치와 보물의 위치는 항상 다르며, 정답이 유일하게 존재함이 보장됩니다.

# # 입력
# # 첫 번째 줄에 정수 $N$과 $M$이 공백으로 구분되어 주어집니다. $(2 ≤ N ≤ 10, 1 ≤ M < N^2)$ 

# # 두 번째 줄부터 $M$개의 줄에 걸쳐 $i$번째 나침반을 사용한 좌표 $X_i, Y_i$와 해당 위치에서의 보물의 방향 $K_i$가 공백으로 구분되어 주어집니다. ($1 ≤ X_i,Y_i ≤ N, 1 ≤ K_i ≤ 8$, $X_i, Y_i, K_i$는 모두 정수입니다.)

# # 출력
# # 보물이 숨겨진 위치의 좌표를 출력해주세요.


# 예제 입력 1 
# 5 10
# 1 1 4
# 1 2 4
# 1 5 6
# 2 3 5
# 3 2 3
# 3 5 7
# 4 5 8
# 5 1 2
# 5 3 1
# 5 4 8
# 예제 출력 1 
# 3 3
# 예제 입력 2 
# 3 2
# 1 2 6
# 3 3 8
# 예제 출력 2 
# 2 1

n, m = map(int, input().split())


list1 = []

ans = [[a, b] for a in range(1, n+1) for b in range(1, n+1)]

#print(ans)

for _ in range(0, m):
    a, b, c = map(int, input().split())
    for i in ans[:]:
        if c == 1:
            ans = [i for i in ans  if i[0] < a and i[1] == b]
        elif c == 2:
            ans = [i for i in ans  if i[0] < a and i[1] > b]
        elif c == 3:
            ans = [i for i in ans  if i[0] == a and i[1] > b]
        elif c == 4:
            ans = [i for i in ans  if i[0] > a and i[1] > b]
        elif c == 5:    
            ans = [i for i in ans  if i[0] > a and i[1] == b]   
        elif c == 6:
            ans = [i for i in ans  if i[0] > a and i[1]  < b]
        elif c == 7:
            ans = [i for i in ans  if i[0] == a and i[1] < b]
        elif c == 8:
            ans = [i for i in ans  if i[0] < a and i[1] < b]

print(*ans[0])