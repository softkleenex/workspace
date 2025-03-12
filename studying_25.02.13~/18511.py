# 문제
# N보다 작거나 같은 자연수 중에서, 집합 K의 원소로만 구성된 가장 큰 수를 출력하는 프로그램을 작성하시오. 
# K의 모든 원소는 1부터 9까지의 자연수로만 구성된다.

# 예를 들어 N=657이고, K={1, 5, 7}일 때 답은 577이다.

# 입력
# 첫째 줄에 N, K의 원소의 개수가 공백을 기준으로 구분되어 자연수로 주어진다. (10 ≤ N ≤ 100,000,000, 1 ≤ K의 원소의 개수 ≤ 3) 둘째 줄에 K의 원소들이 공백을 기준으로 구분되어 주어진다. 각 원소는 1부터 9까지의 자연수다.

# 단, 항상 K의 원소로만 구성된 N보다 작거나 같은 자연수를 만들 수 있는 경우만 입력으로 주어진다.

# 출력
# 첫째 줄에 N보다 작거나 같은 자연수 중에서, K의 원소로만 구성된 가장 큰 수를 출력한다.
import itertools
import math

t, s = map(int, input().split())
s = set(map(int, input().split()))
t_degree = int(math.log10(t) + 1)
#print(t_degree)
#t_degree ~ 1 개의 요소를 뽑자!

data_set = set()

for c in range(t_degree, 0, -1):
    temp_set = set(itertools.product(s, repeat = c))
    for now in temp_set:#set내의 숫자 개수를 통해 숫자 c개를 합치자!
        num = 0
        for i in range(0, len(now)):
            num += 10**(i) * now[i]
        data_set.add(num)

data_list = sorted(list(data_set))

#print(data_list)

min = data_list[0]

for i in data_list:
    if i <= t:
        min = i
    else:
        break

print(min)