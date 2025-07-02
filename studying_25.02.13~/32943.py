#https://www.acmicpc.net/status?user_id=softkleenex&problem_id=32943&from_mine=1

import sys
input = sys.stdin.readline




# 학생수$X$와 좌석의 개수 $C$, 로그의 개수 $K$가 
x, c, k = map(int, input().split())

# 다음 $K$개의 줄에는 학생이 좌석을 신청한 시각 $T$, 학생이 신청한 좌석 번호 $S$, 그리고 학생의 학번 $N$이 공백으로 구분되어 주어진다. 

list1 =[]

for i in range(k):
    list1.append(tuple(map(int, input().split())))

list1.sort(key = lambda x :  x[0])

# print(*list1, sep = '\n')


seats = {i : (0, 0) for i in range(1, c + 1)}#죄석번호 : [이용여부, 학번]
stu_seat = {}


#i는 [시간 좌석번호 학번]
for i in list1:
    seatn = i[1]
    stun = i[2]
    
    if seats[seatn][0] == 1: #고른 좌석에 자리가 있다면
        pass#패스
    else:
        if stun in stu_seat:
            pren_seat = stu_seat[stun]
            seats[pren_seat] = (0, 0)

        seats[seatn] = (1, stun)
        stu_seat[stun] = seatn
        

ans = []


for i in range(1, c + 1):
    if seats[i][0] ==  1:
        ans.append([seats[i][1], i])

ans.sort()

for i in ans:
    print(*i)

# 각 줄에 학번의 오름차순으로 각 학생의 학번과 배정받은 좌석 번호를 공백으로 구분하여 출력한다. 단, 좌석을 신청하지 않았거나, 좌석 신청에 한 번도 성공하지 못한 학생은 출력하지 않는다.