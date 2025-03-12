# 수열 S가 주어졌을 때, 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성하시오.

# 예를 들어, S = [5, 1, 2]인 경우에 1, 2, 3(=1+2), 5, 6(=1+5), 7(=2+5), 8(=1+2+5)을 만들 수 있다. 하지만, 4는 만들 수 없기 때문에 정답은 4이다.

# 입력
# 첫째 줄에 수열 S의 크기 N이 주어진다. (1 ≤ N ≤ 20)

# 둘째 줄에는 수열 S가 주어진다. S를 이루고있는 수는 100,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 출력한다.


import itertools
n = int(input())
s = list()

s = sorted((list(map(int, input().split()))))

res = set()

for usel in range(1, len(s)+ 1):#1 ~ len(s)개의 요소를 이용하는 경우를 모두 세보자! > 2초니까~~
    temp_res = tuple(itertools.combinations(s, usel))
    temp_res =  tuple(sum(i) for i in temp_res)
    #print(temp_res)
    res = res | set(temp_res)

res = sorted([0] + list(res))

#print(res)

if res[1] != 1:
    print('1')
    quit()

for i in range(0, len(res) - 1):
    if res[i + 1] != i + 1:
        print(i + 1)
        quit()


print(res[len(res) -1] + 1)