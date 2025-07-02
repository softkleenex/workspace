# https://www.acmicpc.net/problem/13923

from sys import stdin
input = stdin.readline

uniform = set()

while True:
    #입력은 여러개이므로, try - except문을 이용

    lines =[]
    try:
        n = int(input())
    except:
        break

    for x in range(n):
        lines.append(input().strip())
    
    translines = list(''.join(tup) for tup in zip(*lines))
    # print(type(lines), *lines, sep = '\n')
    # print(type(transline), *transline, sep = '\n')
    
    #n은 3이상이므로, 0, 1이 동일하면 그것이 모범 케이스, 다르다면 2가 모범케이스이다
    
    if set(lines[0]) == set(lines[1]):
        uniform = set(lines[0])
    else:
        uniform = set(lines[2])
    
    
    

    # print(uniform)
    # print(*lines, sep = '\n')
    #각 라인을 for로 탐색한다
    for x in range(n):
        #현재 라인이 모범케이스와 다른경우에 체크, 이떄는 불량라인
        if set(lines[x]) != uniform:
            # print(x, set(lines[x]), uniform, set(lines[x]) != uniform)  
            #불량 라인을 for로 돌리며 체크한다
            for i in range(n):

                #불량라인에서 불량 케이스를 발견한경우
                if set(lines[i]) != uniform:
                    for i2 in range(n):
                        if set(translines[i2]) != uniform:
                        #세로, 가로, 모범라인집합 - 현재라인집합을 출력한다 > 이게 문제인가?
                            print(i + 1, i2 + 1, *(uniform - set(lines[x]) - set(translines[i2])))



