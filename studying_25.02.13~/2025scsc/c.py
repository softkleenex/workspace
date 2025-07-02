#[ 뒤에 [  > 1 / ] > 1 / 2 > 1 / 5 > 1
#] 뒤에 [ > 0 / ]  > 1/ 2 > 1 / 5 > 1
#2 뒤에 [  > 1 / ] > 1 / 2 > 2 / 5 > 1
#5 뒤에 [ > 1 / ] > 1 /  2  > 1 / 5 > 2   
# # 

list1= [
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 2, 1],
        [1, 1, 1, 2]
]

# [ ] 2 5 > 0 1 2 3



a = int(input())

x = input()
x2 = []

for v in x:
    if v == '[':
        x2.append(0)
    elif v == ']':
        x2.append(1)
    elif v == '2':
        x2.append(2)
    elif v == '5':
        x2.append(3)
    else:
        print('error')



ans = 0
pre = x2[0]

for v in x2[1:]:
    now = list1[pre][v]
    ans += now
    pre = v

print(ans)