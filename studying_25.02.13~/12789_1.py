N = int(input())
stu = list(map(int, input().split()))
temp = []
order = 1


for s in stu:
    if s == order:
        order += 1
    else:
        temp.append(s)
while temp:
    if temp[-1] == order:
        temp.pop()
        order += 1
    else:
        break

if temp:
    print('Sad')
    
else:
    print('Nice')
