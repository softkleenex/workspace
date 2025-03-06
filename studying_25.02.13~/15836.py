# 문제
# Matrix multiplication is a basic tool of linear algebra, and has numerous applications in many areas of mathematics, as well as in applied mathematics, computer graphics, physics, and engineering.

# We can only multiply two matrices if their dimensions are compatible, which means the number of columns in the first matrix is the same as the number of rows in the second matrix.

# If A = [aij] is an m×n matrix and B = [bij] is an n×q matrix, the product AB is an m×q matrix. The product AB is defined to be the m×q matrix C = [cij] such that

# \[c_{ij} = \sum_{k=1}^{n}{a_{ik}b_{kj}\]

# Your task is to design a matrix multiplication calculator to multiply two matrices and display the output. If the matrices cannot be multiplied, display "undefined"

# 입력
# The input consists of a few test cases. For each test case, the first line of input is 4 positive integers, M, N, P and Q (1 ≤ M, N, P, Q ≤ 20). M and N represent the dimension of matrix A, while P and Q represent the dimension of matrix B. The following M lines consist of the data for matrix A followed by P lines that contains the data for matrix B as shown in the sample input. The test data ends when M, N, P and Q are 0.

# 출력
# For each test case, the output contains a line in the format "Case #x:", where x is the case number (starting from 1). The following line(s) is the output of the matrix multiplication.

import sys
import math
input = sys.stdin.readline

count = 0

while 1:
    m, n, p, q = map(int, input().split())
    count += 1
    
    if [m, n, p, q] == [0, 0, 0, 0]:
        quit()

    vec1 = []
    vec2 = []
    for i in range(0, m):
        vec1.append(list(map(int, input().split())))
    
    for i in range(0, p):
        vec2.append(list(map(int, input().split())))


    

    print(f"Case #{count}:")

   # print(f"{vec1}\n{vec2}")
    #m * n 인 vec1 과 p q 인 vec2를 곱해 n == p임을 확인한 후, m q인 vec3를 만들어야 한다


            
    if n != p:
        print('undefined')
        continue


    vec3 = []
    a = 0
    for x1 in vec1:
        temp = []
        for x2 in zip(*vec2):
            #print(f"here {x1}, {x2}")
            result = sum(x * y for x, y in zip(x1, x2))
            temp.append(result)
        vec3.append(temp)

    #print(vec3)


    for i in vec3:
        print('| ', end = '')
        print(*i, end = '')
        print(' |')