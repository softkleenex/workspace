# 문제
# 양의 정수로 이루어진 길이가 n인 수열이 있다. 소수 부분 수열이란 길이가 적어도 2이면서, 합이 2보다 크거나 같은 소수가 되는 연속 부분 수열이다.

# 예를 들어, 수열이 [3, 5, 6, 3, 8] 일 때, 길이가 2인 소수 부분 수열이 두 개(5 + 6 = 11, 3 + 8 = 11)이 있고, 길이가 3인 소수 부분 수열은 1개 (6 + 3 + 8 = 17), 길이가 4인 소수 부분 수열은 1개 (3 + 5 + 6 + 3 = 17) 가 있다.

# 수열이 주어졌을 때, 길이가 가장 짧은 소수 부분 수열을 구하는 프로그램을 작성하시오.

# 입력
# 입력의 첫째 줄에는 테스트 케이스의 개수 t (1 ≤ t ≤ 20) 가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있고, 줄의 첫 번째 정수 n은 (0 < n ≤ 10000) 수열의 길이이다. 다음에 주어지는 정수 n개는 수열의 원소이다. 수열의 원소는 10000보다 작거나 같은 음이 아닌 정수이다.

# 출력
# 각 테스트 케이스마다 가장 짧은 소수 부분 수열의 길이가 x라면 "Shortest primed subsequence is length x:"를 출력하고, 그 수열 공백으로 구분해 출력한다. 가장 짧은 소수 부분 수열이 여러 가지면, 먼저 나오는 것을 출력한다.

# 소수 부분 수열이 없는 경우에는 "This sequence is anti-primed."를 출력한다.

import sys
import itertools
import math
from collections import deque
input = sys.stdin.readline


def sliding_windows_deque(lst, x):
    dq = deque(lst[:x], maxlen=x)  # 처음 x개를 deque에 담음
    result = [list(dq)]

    for item in lst[x:]:  
        dq.append(item)  # O(1) 연산으로 윈도우 이동
        result.append(list(dq))
    return result



# def is_prime(s):#s가 소수인지 판별해야 한다 s가 2 ~ s의 제곱근 까지의 것과 나눠지지 않으면 소수임
#     if (s in prime_set):
#         return True
#     else:
#         return False


def is_prime(s):#s가 소수인지 판별해야 한다 s가 2 ~ s의 제곱근 까지의 것과 나눠지지 않으면 소수임, s는 최솟값 2
    if s < 2:
        return False
    if s in (2, 3):
        return True
    if s % 2 == 0 or s % 3 == 0:
        return False
    if all  (s % i3 != 0  for i3 in range(5, int(math.sqrt(s) + 1), 2   )  ):
        return True
    
    return False

def shortest_primed_subsequence(lst):
    n = len(lst)
    prefix_sum = [0] * (n + 1)
    for i in range(0, n):
        prefix_sum[i + 1] = prefix_sum[i] + lst[i]#perfix_sum i > lst 0 ~ i-1 까지의 총합

    for length in range(2, n+1):
        #lst를 이용해 길이가 lenght 인 것들을 만들자!        
        for start in range(n -length + 1):
            #시작점 지정, 0 ~ lenght -1  > n - lenght ~ n - length + length = n
            end = start + length#끝점을 지정하는데, 끝점의 직전까지가 방문할 인덱스이다
            sub_sum = prefix_sum[end] - prefix_sum[start]
            #end의 이전까지가 방문할 인덱스고, perfix[x]는 x직전값까지의 누적합을 다루기에, perfix_sum[end]가 유효하다
            if is_prime(sub_sum):
                return length, lst[start:end]
            
    return None

# prime_set = set([2, 3])
# temp = 1
# while temp * 6 -1 <= (   10000 * 10000  ):
#     temp_ans = temp * 6
#     prime_set.add(temp_ans -1)
#     prime_set.add(temp_ans+ 1)
#     temp += 1






n = int(input())
for _ in range(0, n):
    list1 = list(map(int, input().split()))
    list1.pop(0)
    ans = shortest_primed_subsequence(list1)
    if ans:
        print(f'Shortest primed subsequence is length {ans[0]}:', *ans[1])
    else:
        print('This sequence is anti-primed.')