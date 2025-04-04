# 문제
# Games that are commonly found in the Unix System during the 70s and 80s are design in text mode. Grid is the basic layout for many of these games where pieces or items are positioned in rows and columns. Classic examples would be tic-tac-toe, chess and minesweeper. You are to design a simple text-based grid layout engine that can be used in the games.

# Given specified dimensions, print a text-based grid pattern. Use the | (pipe) sign to print vertical elements, the – (minus) to print horizontal ones and + (plus) for crossing. The rest of the spaces are filled with * (asterisk).

# 입력
# The first line of input contains a positive integer N (N ≤ 100) which indicates the number of test cases. Each of the following N lines contains four positive integers: row – the number of rows, col – the number of columns, w and h – the width and height of the single grid respectively. (1 ≤ row, col ≤ 10; 1 ≤  w, h ≤ 5 )

# 출력
# For each test case, output a line in the format "Case #x:" where x is the case number (starting from 1), follow by the grid pattern as shown in the sample output.

import sys

input = sys.stdin.readline


n = int(input())

for _ in range(0, n):
    case = _ + 1
    print(f'Case #{case}:')
    #row, col, w, h = map(int, input().split())#차예대로 행, 열, 단일 그리드의 너비(가로), 높이(세로)
    h, w, col, row = map(int, input().split())#차예대로 행, 열, 단일 그리드의 너비(가로), 높이(세로)



    floor = (['+'] +  (['-'] * col)) * w  + ['+']
    
    grid1 = [['*'] * col] * row
    

    print(*floor, sep ='')
    for i in range(0, h):
        for i2 in grid1:
            for i3 in range(w):
                print('|', end = '')
                print(*i2, sep = '', end = '')
            print('|')
        print(*floor, sep = '')
        

   