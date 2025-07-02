# https://www.acmicpc.net/contest/problem/1479/3

n = int(input())
c = int(input())
fishes = []

for i in range(n):
    #물고기의 먹성 x, 크기 s, 가격 w이
    fish = list(map(int, input().split()))
                    
    fishes.append(fish)


fishes.sort(key = lambda x :  x[0])


ans = 0

for i in range(len(fishes)):
    cost = sum(i[2] - i[0] * c  for i in fishes[:i + 1])
    ans = max(cost, ans)

print(ans)