# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	6713	2032	1659	35.685%
# 문제
# 정수 N이 주어졌을 때, N의 제곱근을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 양의 정수 N이 주어진다. 정수 N의 제곱근은 항상 정수이며, N의 길이는 800자리를 넘지 않는다.

# 출력


import math

a = int(input())

def sqrt(front, back, n):
    
    mid = (front + back) // 2
    
    while mid ** 2 != n:
        if mid ** 2 <  n: # 늘려야한다
            front = mid
            back = back
            mid = (front + back) // 2
            
        elif mid ** 2 > n:#줄여야 한다
            front = front
            back = mid
            mid = (front + back) // 2
        

    return mid


print(sqrt(1, a, a))#front, back, target