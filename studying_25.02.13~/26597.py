import sys
input = sys.stdin.readline

q = int(input())

b = pow(10, 18) + 1
a = - b

#a초과 b 미만이 간격, 이 간격이 1 이되면 알수 있다, b - a == 1, 1 - (-1)  == 2 (0이 최애)
#모순은 !(b - a >= 1) 이면 될듯

ans = 0

for i in range(1, q+1):
    x = input().split()
    x, y = int(x[0]), x[1]
    # print(x, y)
    if y == '^':#a를 갱신
        a = max(a, x)

    elif y == 'v':#b를 갱신
        b = min(b, x)

    else:
        print("????")   




    if not(b - a >= 2):
        if (ans >= 0):
            ans = -i




    elif b - a == 2: 
        if ans == 0: #모순이면 알아냄의 의미 x
            ans = i
            #print(x, y)
    







if ans == 0:
    print('Hmm...')
elif ans < 0:
        print('Paradox!')
        print(-ans)
else:
    print('I got it!')
    print(ans)


    
