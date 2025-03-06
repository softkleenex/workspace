# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

# 출력
# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.


import math
import sys
import itertools
input = sys.stdin.readline

def f1(dict1):
    x = dict1[1]
    y = dict1[2]
    z = dict1[3]
    
    ans = math.factorial(x + y + z) / (math.factorial(x) if x == 0 else 0 + math.factorial(y) if y == 0 else 0+ 
                                       math.factorial(z) if z == 0 else 0 )
    return ans



t = int(input())

list1 = [0] * 12



list1[1] = 1 # {1:1, 2:0, 3:0}
list1[2] = 2 # {1: 2, 2: 0, 3: 0}, {1: 0, 2:1, 3:0}
list1[3] = 4 # {1 : 3, 2: 0, 3: 0}, {1: 1, 2:1, 3:0}, {1:0, 2:0, 3:1}
for i in range(4, 12):
    list1[i] += (list1[i-1] + list1[i-2] + list1[i-3])

for _ in range(0, t):
    temp = int(input())
    print(list1[temp])
