# 문제
# 길이 $N$인 양의 정수열 $A_1, \dots , A_N$이 주어진다. 이 수열을 오름차순으로 만들려 한다. 수열 $A_1, \dots , A_N$이 오름차순이라는 것은, 각 $i$ ($1 ≤ i ≤ N - 1$)에 대해 $A_i ≤ A_{i+1}$이라는 것이다.

# 수열 $A$를 오름차순으로 만들기 위해, 수열 $A$에 다음 연산을 몇 번이든 반복해서 적용할 수 있다.

# 어떤 $i$ ($1 ≤ i ≤ N$)에 대해 $A_i$에 $2$를 곱한다.
# 연산을 최소 횟수로 적용해서 $A$를 오름차순으로 만들고 싶다. 이때, 최소 횟수를 구하라.

# 입력
# 첫 번째 줄에 $N$이 주어진다.

# 두 번째 줄에 $A_1, \dots , A_N$이 주어진다.

# 출력
# 첫 번째 줄에 답을 출력한다.

# 제한
# 주어지는 모든 수는 정수이다.
#  $1 ≤ N ≤ 250\, 000$ 
#  $1 ≤ A_i ≤ 1\, 000\, 000$ ($1 ≤ i ≤ N$)
# 서브태스크
# 번호	배점	제한
# 1	12	
# 각 $i$ ($1 ≤ i ≤ N$)에 대해, $A_i = 1$ 또는 $A_i = 2$ 
# 2	10	
# 각 $i$ ($1 ≤ i ≤ N$)에 대해, $A_i = 2^{k_i}$를 만족하는 $0$ 이상의 정수 $k_i$가 존재
# 3	11	
#  $N ≤ 10$ 
# 4	19	
# 각 $i$ ($1 ≤ i ≤ N$)에 대해, $A_i = 2$ 또는 $A_i = 3$ 
# 5	20	
# 각 $i$ ($1 ≤ i ≤ N - 1$)에 대해, $A_i ≥ A_{i+1}$ 
# 6	28	
# 추가 제약 조건 없음



# 예제 입력 1 
# 5
# 3 1 4 1 5
# 예제 출력 1 
# 4
#  $A_2$, $A_4$에 각각 두 번씩 연산을 적용하면 된다. 연산을 적용한 이후에 수열 $A$는 $[3, 4, 4, 4, 5]$가 된다.

# 예제 입력 2 
# 5
# 3 1 5 1 5
# 예제 출력 2 
# 6
#  $A_2$에 두 번, $A_4$에 세 번, $A_5$에 한 번 연산을 적용하면 된다. 연산을 적용한 이후에 수열 $A$는 $[3, 4, 5, 8, 10]$가 된다.

# 예제 입력 3 
# 5
# 1 2 3 4 5
# 예제 출력 3 
# 0


import sys
input = sys.stdin.readline

import math

n = int(input())

inputlist = list(map(int, input().split()))
check = [0 for i in inputlist]
reallist = [inputlist[0]] + [0 for i in inputlist[1:]]

# reallist[0] = 1
# reallist[1] = 1
# print(reallist)
# check[0] = 1
# print(check)

count = 0

for i1 in range(1, len(inputlist)):
    if math.log2(inputlist[i1 - 1]) + check[i1-1] > math.log2(inputlist[i1]) + check[i1]:
        #이전의 값
        check[i1] = math.ceil(math.log2(inputlist[i1 - 1]) -  math.log2(inputlist[i1])  + check[i1 -1])
        count += check[i1]

    #reallist[i1] = inputlist[i1] * pow(2, check[i1])


# print(check)
# print(reallist)
print(count)

