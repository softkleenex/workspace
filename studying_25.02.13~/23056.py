# https://www.acmicpc.net/problem/23056


from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

stus = dict()

for i in range(1, n+1):
    stus[i] = []

while True:
    x, y = input().split()
    x = int(x)
    if x == 0 and int(y) == 0:
        break
    else:
        if len(stus[x]) < m:
            stus[x].append(y)


for x in range(1, n + 1, 2):
    stus[x].sort(key = lambda k : [len(k), k])
    for x2 in stus[x]:
        print(x, x2)


for x in range(2, n+2, 2):
    stus[x].sort(key = lambda k : [len(k), k])
    for x2 in stus[x]:
        print(x, x2)
    
