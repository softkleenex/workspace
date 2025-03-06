# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	648	300	246	45.471%
# 문제
# Anna and Bob are starting up a new high-tech company. Of course, one of their key considerations is choosing a good name for the company. Palindromes are cool. (A palindrome is a word that is the same when reversed, like the names of our two entrepreneurs.) They would really the name of their company to be a palindrome. Unfortunately, they cannot think of a nifty company name that is also a palindrome.

# Maybe at least the telephone number of their company could be a palindrome. However, they really want their customers to be able to call them, so they want to choose the company name so that, when it is typed using the letters printed on a phone keypad, the result is also their phone number. (On a standard phone keypad, the following keys contain the corresponding letters: 2: ABC, 3: DEF, 4: GHI, 5: JKL, 6: MNO, 7: PQRS, 8: TUV, 9: WXYZ.)

# 입력
# The first line of input contains a single integer, the number of lines to follow. Each following line contains a company name, which is a string of at most 20 letters, which may be either uppercase or lowercase.

# 출력
# For each company name, print a single line of output, containing the word YES if the phone number is a palindrome, or NO if it is no


#2: ABC, 3: DEF, 4: GHI, 5: JKL, 6: MNO, 7: PQRS, 8: TUV, 9: WXYZ

import sys
input = sys.stdin.readline

dict1 = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}
for i in dict1:
    dict1[i] = list(''.join(dict1[i]))

#print(dict1, sep = '\n')

dict2 = {}

for num, spells  in dict1.items():
    for spell in spells:
        dict2[spell] = num

#print(dict2)
n = int(input())

for i in range(0, n):
    name = list(''.join(input().split()))#name에는 문자열이 들어있다.
    for i in range(0, len(name)):#i는 name을 분해한, 단어 하나를 나타낸다
        name[i] = chr(ord(name[i]) -( ord('a') - ord('A'))) if ord(name[i]) >= ord('a') else name[i] #소문자라면 대문자로 바꾼다
        #print(name[i])
        i = dict2[name[i]]
    for i in range(0, len(name)):
        name[i] = dict2[name[i]]


    if name == name[::-1]:
        print('YES')
    else:
        print('NO')
