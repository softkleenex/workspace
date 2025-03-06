# 문제
# 양의 정수 N개로 이루어진 수열 A가 있다. 상근이는 수열 A의 모든 두 수의 합을 알고 있다. 이때, 수열 A를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수열의 크기 N이 주어진다. (2 ≤ N ≤ 1000)

# 다음 N개 줄에는 100,000보다 작거나 같은 양의 정수가 N개씩 주어진다. 이 숫자들은 S를 이루는 숫자이며, S(i,j) = A[i] + A[j] (i≠j), S(i,j) = 0 (i=j) 이다. S(i,j)는 i번째 줄, j번째 숫자를 의미하며, A[i]는 A의 i번째 수이다.

# 입력으로 주어지는 S에 해당하는 수열 A는 항상 유일하다.

import sys

input = sys.stdin.readline

n = int(input())

a1 = []

for i in range(0 ,n):
    a1.append(list(map(int, input().split())))


if n == 1 :
    print(a1, sep = ' ')
elif n == 2:
    print("1 1")

if n == 1 or n == 2:
    quit()

    
s = sum((sum(x) for x in a1)) // (2*n - 2)

s2 = []

for i in zip(*a1):
    s2.append((sum(i) - s) // (n -2))



print(*s2, sep = ' ')