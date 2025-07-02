#이름,전화번호,이메일,주소,생년월일


list1 = []

with open('/Users/isangjae/workspace/studying_25.02.13~/가상주소록_100명_생년월일포함.csv', encoding='utf-8') as f:
    next(f) 
    for line in f:
        line = line.strip()
        if line == '':
            continue
        list1.append(line.split(','))





# print(*list1, sep = '\n')


date = [[] for i in range(10000)]

for i, v in enumerate(list1):
    temp = int(v[4][4:])
    date[temp].append(list1[i])




# print(*date, sep = '\n')

i = 0
t = len(date)


# print(*date, sep = '\n')



for v in date:
    if len(v) > 0:
        nowdate = int(v[0][4])
        # print(nowdate)
        month = (nowdate // 100) % 100
        date = nowdate % 100
        people = len(v)
        print(f'{month} 월 {date} 일, 중복자 {people} 명')
        print(*v, sep = '\n')
        print()