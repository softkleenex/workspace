# https://www.acmicpc.net/problem/3098

from sys import stdin
input = stdin.readline

from collections import deque

n, m = map(int, input().split())

f = dict()
for x in range(1, n + 1):
    f[x] = set()

for x in range(m):
    a, b = map(int, input().split())
    f[a].add(b)
    f[b].add(a)



ans = [0]
c = 0


while True:
    
    

    new = deque()

    for x in f.keys():#x가 현재 대상
        for x2 in f[x]:#x의 친구들을 순회하며
            for x3 in f[x2]:#x의 친구들의 친구와 x를 연결한다
                if x3 not in f[x] and x != x3:#자기 자신 제외, 새로운 친구만!
                    new.append((x, x3))
            

    
    new = set(new)
    new = deque(new)
    count = (len(new) // 2)
    


    while new:
        x, x2 = new.popleft()
        f[x].add(x2)
        f[x2].add(x)
 

    if count == 0:
        break
    else:
        c += 1
        ans.append(count)
        


ans[0] = c

print(*ans, sep = '\n')