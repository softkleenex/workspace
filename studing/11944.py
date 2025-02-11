'''
문제
문제는 매우 간단하다. N을 N번 출력하는 프로그램을 작성하여라. 다만, 답이 길어지는 경우 답의 앞 M자리만 출력한다.

입력
첫 번째 줄에는 N, M이 주어진다. (1 ≤ N, M ≤ 2016)

출력
N을 N번 출력한다. 만약 답이 길어지면 답의 앞 M자리를 출력한다.

예제 입력 1 
20 16
예제 출력 1 
2020202020202020
'''


N, M = list(map(int, input().split()))

N_list = str(N) * (M // len(str(N)) + 1) 

N_list = N_list[:min(N * len(str(N)), M)]

print(N_list)