
# A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
# 3	2	1	2	3	3	3	3	1	1	3	1	3	3	1	2	2	2	1	2	1	1	2	2	2	1
# 입력
# 첫째 줄에 알파벳 대문자로만 이루어진 길이 K(1 ≤ K ≤ 1,000,000)인 문자열 S가 주어진다.

# 출력
# 첫째 줄에 정답을 출력한다.

# 마지막으로 남은 수가 홀수라면 "I'm a winner!"를 출력하고 0이거나 짝수라면 "You're the winner?"를 출력한다.
# # 3	2	1	2	3	3	3	3	1	1	3	1	3	3	1	2	2	2	1	2	1	1	2	2	2	1

import math

#def make(list1):
    

ans = {}
ans = dict(zip(map(chr, range(ord('A'), ord('Z')+1)), "3	2	1	2	3	3	3	3	1	1	3	1	3	3	1	2	2	2	1	2	1	1	2	2	2	1".split()))

#print(ans)

n = list(''.join(input()))

sum = 0

for i in range(0, len(n)):
    sum += int(ans.get(n[i]))

if (sum %2 != 0):
    print("I'm a winner!")
else:
    print("You're the winner?")
