# https://www.acmicpc.net/problem/25594

list1 = list('''
a	aespa
b	baekjoon
c	cau
d	debug
e	edge
f	firefox
g	golang
h	haegang
i	iu
j	java
k	kotlin
l	lol
m	mips
n	null
o	os
p	python
q	query
r	roka
s	solvedac
t	tod
u	unix
v	virus
w	whale
x	xcode
y	yahoo
z	zebra'''.split())


dict1 = dict()

for i in range(0, len(list1), 2):
    dict1[list1[i]] = list1[i + 1]

s = list(input().strip())

ans = []


for i in range(0, len(s)):
    if s[i] == '0':
        continue

    


    if dict1[s[i]] == ''.join(s[i:  i + len(dict1[s[i]])]):
        ans.append(s[i])
        for i2 in range(0, len(dict1[s[i]])):
            s[i + i2] = '0'


    else:
        # print(s[i])
        # print(dict1[s[i]])
        # print(''.join(s[i:  i + len(dict1[s[i]])]))

        print('ERROR!')
        exit(0)





print('''It's HG!''')
print(*ans, sep = '')