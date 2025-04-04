# 문제
# 길이가 $N$인 수열 $A_1, \cdots, A_N$이 주어집니다. 수열의 모든 수는 서로 다른 $1$ 이상 $N$ 이하의 수입니다. 아래 조건을 모두 만족시키는 $(i, j)$ 정수쌍의 개수를 구하세요.

#  $1 \le i \le j \le N$.
#  $A$의 $i$번째 수부터 $j$번째 수까지가 오름차순으로 배열되어있다. 즉, $i \le k < j$를 만족하는 모든 정수 $k$에 대해 $A_k < A_{k+1}$.
# 입력
# 첫 줄에 수열의 길이 $N$이 주어집니다. $(1 \le N \le 200\,000)$ 

# 다음 줄에는 수열의 각 원소 $A_1, A_2, \cdots, A_N$이 공백으로 구분되어 주어집니다. $(1 \le A_i \le N;$ $A_1, A_2, \cdots, A_N$은 서로 다른 정수$)$ 

# 출력
# 문제의 조건을 만족시키는 $(i, j)$ 정수쌍의 개수를 출력하세요.

import sys
input = sys.stdin.readline

import math

n = int(input())

list1 = list(map(int, input().split()))
#print(list1)

list2 = [1] * n







for i in range(1, n):

    if list1[i] > list1[i - 1]:#이전보다 현재가 크면
        list2[i] = list2[i - 1] + 1
        list2[i-1] =  1
    else:
        list2[i] = 1



ans = n #길이 1개짜리 경우는 미리 생각

ans_list = []

ans_list = [i for i in list2 if i != 0]

for i in ans_list:
    ans += math.comb(i, 2) #i개 중에 2개를 중복없이 선택하는 갯수는? i C 2

print(ans)

