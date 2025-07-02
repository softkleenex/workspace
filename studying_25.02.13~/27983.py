
# 당신은 수직선 위에 묶여 있는 $N$개의 리본들을 받았다. $i$번 $(1 \leq i \leq N)$ 리본은 수직선의 점 $X_i$에 묶여 있고, 길이는 $L_i$이다. 또한, 그 리본의 색은 $C_i$이며 R, Y, B 중 하나이다. (R, Y, B는 각각 빨강, 노랑, 파랑을 나타낸다.)

# 이제 당신은 리본 두 개를 골라서 매듭을 지으려고 한다. 리본의 탄성이 좋지 않아서 길이를 늘릴 수는 없지만, 구부릴 수는 있다. 즉, $\lvert X_i - X_j \rvert \le L_i + L_j$ $(i \ne j)$ 를 만족한다면 $i$번째와 $j$번째 리본으로 매듭을 지을 수 있다. (리본은 면적이 없는 선으로 가정하고 매듭 길이는 무시한다.) 묶인 매듭은 두 리본의 색이 다를 때, 즉 $C_i \ne C_j$일 때 아름다운 매듭이라고 부른다.

# 아름다운 매듭을 지을 수 있는 두 리본의 번호를 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 정수 $N$이 주어진다.

# 두 번째 줄에 $N$개의 정수 $X_1$, $X_2$, $\cdots$, $X_N$이 주어진다.

# 세 번째 줄에 $N$개의 정수 $L_1$, $L_2$, $\cdots$, $L_N$이 주어진다.

# 네 번째 줄에 $N$개의 문자 $C_1$, $C_2$, $\cdots$, $C_N$이 주어진다.

# 출력
# 첫 번째 줄에 정답이 존재한다면 YES, 아니라면 NO를 출력한다.

# 정답이 존재한다면 두 번째 줄에 아름다운 매듭을 지을 수 있는 두 리본의 번호를 출력한다.

# 답이 여러 개 존재한다면 아무거나 출력해도 상관없다.

# 제한
#  $\color{red}{2 \le N \le 10^3}$ 
#  $-10^9 \le X_1 < X_2 < \cdots < X_{N} \le 10^9$ 
#  $1 \le L_i \le 10^9$ 
#  $C_i \in \{$ R, Y, B $\}$ 
# 예제 입력 1 
# 2
# 1 3
# 1 1
# Y R
# 예제 출력 1 
# YES
# 1 2
# 예제 입력 2 
# 2
# -4 1
# 1 2
# B B
# 예제 출력 2 
# NO


riboon = []

n = int(input())

for i in range(3):
    if i  < 2:
        riboon.append(list(map(int, input().split())))
    if i == 2:
        riboon.append(input().split())

# print(*riboon, sep = '\n')
# print()



riboon2 = [list(x) for x in zip(*riboon)]

# print(*riboon2, sep = '\n')

ans = []

for i in range(n):
    now = riboon2[i]
    target = riboon2[0 : i] + riboon2[i + 1 : len(riboon2)]
    for i2 in target:
        if abs(now[0] - i2[0]) <= now[1] + i2[1] and now[2] != i2[2]:
            print('YES')
            print(i + 1, riboon2.index(i2) + 1)
            quit()

print('NO')