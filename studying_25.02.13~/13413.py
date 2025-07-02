from collections import Counter
from sys import stdin

input = stdin.readline

def check(now, target):
    jobs = 0

    #다른거 2개에 대해서 < 그 돌들의 색깔이 다르면 서로서로 바꾸면 되잖아?
    diff = list(zip(now, target))
    diff = Counter([x[0] for x in diff if x[0] != x[1]])
    while diff['B'] >= 1 and diff['W'] >= 1:
        jobs += 1
        diff['B'] -= 1
        diff['W'] -= 1
    
    while diff['B'] >= 1:
        jobs += 1
        diff['B'] -= 1

    while diff['W'] >= 1:
        jobs += 1
        diff['W'] -= 1
    
    return jobs
        

n = int(input())

for _ in range(n):
    t = int(input())
    nowstones = input()
    targetstones = input()
    print(check(nowstones, targetstones))