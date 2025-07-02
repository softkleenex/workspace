# https://www.acmicpc.net/problem/4378

list0 = ' '.join('`1234567890-=').split()
list1 = (' '.join('QWERTYUIOP[]\\')).split()
list2 = (' '.join('ASDFGHJKL;\'')).split()
list3 = (' '.join('ZXCVBNM,./')).split()

changespell = list0 + list1 + list2 + list3

# print(*changespell)

while True:
    try:
        xinput = input()
        for x in xinput:
            if x in changespell:
                print(changespell[changespell.index(x) - 1], end = '')
            elif x == ' ':
                print(' ', end = '')
        print()

    except:
        exit()