# https://www.acmicpc.net/problem/10469

from collections import deque

chess = list()

queenidxs = deque()

for i in range(8):
    chess.append(input())
    for i1, v1 in enumerate(chess[i]):
        if v1 == '*':
            queenidxs.append([i, i1])



if len(queenidxs) != 8:
    print('invalid')
    exit()

directs = [[-1, -1], [+1, +1], [-1 , +1], [+1, -1], [+1, 0], [-1, 0], [0, -1], [0, +1]]


def check(x, y, direct):

    while True:
        
        x += direct[0]
        y += direct[1]
        
        if 0 <= x <= 7 and 0 <= y <= 7:
            if chess[x][y] == '*':
                print('invalid')
                exit()
        else:
            break
            



while queenidxs:
    x, y = queenidxs.popleft()
    for direct in directs:
        check(x, y, direct)




print('valid')