import math

# 문제의 개수, 문제를 맞출 확률, 문제를 푸는 데 걸리는 시간, 답을 기입하는 데 걸리는 시간, 정답이 나올 때까지 기다리는 시간
num_problems, prob_correct, time_solve, time_submit, time_wait = 300, 0.98, 10, 1, 50

# 최적의 n 값을 찾기 위한 변수들
min_time = float('inf')
optimal_n = 1

for n in range(1, num_problems + 1):
    num_sets = num_problems // n
    remainder = num_problems % n
    time_per_set = (n * (time_solve + time_submit) + time_wait) / prob_correct
    time_total = (num_sets + remainder) * time_per_set
        
    print(f'n={n}, 소요시간={time_total}초')
        
    if time_total < min_time:
        min_time = time_total
        optimal_n = n

print(f'최적의 n={optimal_n}, 이때의 전체 문제를 모두 맞추기 위해 필요한 시간(초)의 기대값={min_time:.1f}초')
