# 문제
# We consider a number to be beautiful if it consists only of the digit 1 repeated one or more times. Not all numbers are beautiful, but we can make any base 10 positive integer beautiful by writing it in another base.

# Given an integer N, can you find a base B (with B > 1) to write it in such that all of its digits become 1? If there are multiple bases that satisfy this property, choose the one that maximizes the number of 1 digits.

# 입력
# The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of one line with an integer N.

# Limits

# 1 ≤ T ≤ 100.
# 3 ≤ N ≤ 1000.
# 출력
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the base described in the problem statement.

# 예제 입력 1 
# 2
# 3
# 13

# 예제 출력 1 
# Case #1: 2
# Case #2: 3
# 힌트
# In case #1, the optimal solution is to write 3 as 11 in base 2.

# In case #2, the optimal solution is to write 13 as 111 in base 3. Note that we could also write 13 as 11 in base 12, but neither of those representations has as many 1s.

import collections

def base(n, i): #숫자 n 을 i 진수로 바꿔주자
    n = int(n)
    ans = []


    while(n > 0):
        ans =  [n % i] + ans
        n = n // i

    if all (i == 1 for i in ans):
        return (ans.count(1), i)
    
    return (0 ,0)
        


t = int(input())

for t1  in  range(t):
    n = input()
    
    max_base = (0, 0)
    for i in range(2, int(n) + 1):
        temp_ans = base(n, i)

        max_base = max_base if max_base[0] > temp_ans[0] else temp_ans
    
    print(f'Case #{t1 + 1}: {max_base[1]}')
        