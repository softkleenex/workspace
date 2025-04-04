# # 문제
# # 영웅이는 2의 거듭제곱을 좋아해서 A를 최대한 많은 항의 2의 거듭제곱의 합으로 표현한다. 표현된 2의 거듭제곱은 지수가 0 이상의 서로 다른 정수이다.

# # 예를 들어 31은 5개의 항으로 표현된다. 우리는 이것을 영웅이의 표현법이라고 부를 것이다.

# # N개의 자연수 A1, A2, ..., AN이 주어진다. 이 중 최대 한 개의 자연수를 제거하고, 나머지를 영웅이의 표현법으로 나타내자.

# # 그 후 각 정수 x에 대해 2x가 홀수 개 존재하면 2x를 더하고, 짝수 개 존재하면 더하지 않는다. 이렇게 했을 때 얻을 수 있는 최대 합을 2번 출력하라.

# # 입력
# # 첫째 줄에 자연수 N (1 ≤ N ≤ 2,222,222)이 주어지고, 둘째 줄에는 N개의 자연수 A (1 ≤ A ≤ 2,222,222)가 주어진다.

# # 출력
# # 최댓값을 2번 연속해서 출력한다.



# 예제 입력 1 
# 3
# 5 7 11
# 예제 출력 1 
# 1414
# 예제 입력 2 
# 3
# 1 2 4
# 예제 출력 2 
# 77

import math
import collections
import sys
input = sys.stdin.readline

n = int(input())

input_list =  list(map(int, input().split()))

max_n = 1

while True:
    if max_n < 2222222:
        max_n *= 2
    else:
        break


original_xor = 0

for a in input_list:
    original_xor ^= a

all_val = original_xor

for a in input_list:
    new_xor = original_xor ^ a
    all_val = max(all_val, new_xor)

print(f'{all_val}{all_val}')
