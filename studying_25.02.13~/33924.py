n, m = map(int, input().split())
k = int(input())

skills = input()





def skill(x, n, m):
    if x == 'A':      
        n = (n + 2)
        if n > 4:
            n -= 4

    elif x == 'B':
        if n % 2 == 1:
            n += 1
        else:
           n -= 1

        m = (m + 1)

        if m > 2:
            m = 1

    elif x == 'C':
        if n == 1:
            n = 4
        elif n == 2:
            n = 3
        elif n == 3:
            n = 2
        elif n == 4:
            n = 1

        m = (m + 1)
        if m > 2:
            m -= 2
        
        

    elif x == 'D':
        if n == 1 and m == 1:
            m = 2
        elif n == 4 and m == 2:
            m = 1
        
        elif m == 1:
            n -= 1
        elif m == 2:
            n += 1

    return n, m

for x in skills:
    # print(n, m)
    n, m = skill(x, n, m)

print(n, m)