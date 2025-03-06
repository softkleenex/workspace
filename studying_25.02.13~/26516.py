# A “Mutint” is an integer M that is changed according to certain criteria, such as in this problem. Given a positive integer, change M according to the following rules.

# Find the leftmost largest digit D of M.
# If D is odd, change it to a zero.
# If D is even, add 4 to that digit. If the sum exceeds 9, change D to the one’s place of the sum.
# 입력
# Several integers, each on one line. The end of input is signaled with a zero on the last line. All integers, except the last integer, are positive.

# 출력
# M, according to the rules above. M cannot have leading zeros.

a = -1

while 1:
    a = map(str, input())
    
    a = ''.join(a)
    
    a = list(map(int, a))
    
    #print(a)

    if a == [0]:
        quit()
    
    #print(a.index(max(a)))
    if max(a) % 2 == 1:
        a[a.index(max(a))] = 0
    else:
        temp = (max(a) + 4)% 10
        a[a.index(max(a))] = temp
    try:
        while(a[0] == 0):
            a.pop(0)
    except:
        pass
    
    print(*a, sep = '')