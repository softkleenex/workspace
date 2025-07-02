#전주곡 다시- 20분간(11시 30분까지)
N, M = map(int, input().split())

dict1={}

for i in range(N):
    num, title, *rest = input().split()
    dict1[title] = ' '.join(rest[:3])



# print(*dict1.items(), sep = '\n')


for i in range(M):
    music = input()
    dict2 =dict((i, 0) for i in dict1.keys())



    for title, value in dict1.items():
        if music in value:
            if len(dict2.values())==0:
                dict2[title]=1
            else:
                dict2[title]+=1
        else:
            dict2[title]=0


            
    if len(dict2.values()) >= 2:
        print('?')
    elif len(dict2.values()) == 1:
        print(list(dict2)[0])
    else:
        print('!')