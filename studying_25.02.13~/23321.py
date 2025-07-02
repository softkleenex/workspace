
# 10년 전, 홍익대학교 학생을 위한 댄스파티가 개최되었다.

#  	도약 준비	도약 중	착석
# 1	.	o	.
# 2	o	w	.
# 3	m	l	o
# 4	l	n	L
# 5	n	.	n
# 댄스파티에는 위와 같이 세 종류의 학생이 있다.

# 학생들은 빈자리 없이 좌우로 딱 붙어 한 줄로 서서, 다음 차례가 되면 도약 준비 학생은 도약 중으로, 도약 중 학생은 도약 준비로 바뀐다. 착석 학생은 바뀌지 않는다.

# 당신은 댄스파티의 모습을 한 장의 사진에 담았다.

# 그리고 10년이 흐른 지금, 대학을 졸업하고 사회인이 된 당신은 짐을 정리하던 도중 댄스파티의 사진을 발견하였다. 그 낡은 단 한 장의 사진은 하루가 바쁘게 일상에 치이며 살아가는 당신을 추억에 잠기게 하기에 충분하였다.

# 그 시절을 회상하기 위해 주어진 사진을 토대로 다음 차례의 모습을 유추하라.

# 입력
# 댄스파티의 사진이 $5$줄의 문자열로 주어진다.

# 각 줄의 최대 길이는 $10\,000$자이며 모든 줄의 길이는 동일하다.

# 각 열은 도약 준비, 도약 중, 착석 중 하나이다.

# 출력
# 입력으로 주어진 댄스파티 사진의 다음 차례의 모습을 $5$줄의 문자열로 출력한다.

# 예제 입력 1 
# .o.
# ow.
# mlo
# lnL
# n.n
# 예제 출력 1 
# o..
# wo.
# lmo
# nlL
# .nn
# 예제 입력 2 
# .
# o
# m
# l
# n
# 예제 출력 2 
# o
# w
# l
# n
# .
# 예제 입력 3 
# .....
# oo.oo
# mmomm
# llLll
# nnnnn
# 예제 출력 3 
# oo.oo
# ww.ww
# lloll
# nnLnn
# ..n..


type1 = ('.', 'o' , 'm', 'l' , 'n')
type2 = ('o', 'w' , 'l', 'n' , '.')
type3 = ('.', '.' , 'o', 'L' , 'n')

list1 = []

for _ in range(5):
    list1.append((' '.join(input())).split())




# print(list1)





list2 = list(zip(*list1))
#print(*list2, sep = '\n')

for i in range(len(list2)):
    if list2[i] == type1:
        list2[i] = type2
    elif list2[i] == type2:
        list2[i] = type1
    elif list2[i] == type3:
        list2[i] = type3
    else:
        print(list2[i], 'what')

list2 = list(zip(*list2))

for i in list2:
    print(*i, sep = '')