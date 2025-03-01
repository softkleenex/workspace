inputValue = int(input())
a = 0
b = 0


def div():
    i = 0
    testi = inputValue
    while testi % 2 == 0 or testi % 3 == 0:
        if testi % 2 == 0:
            testi = testi / 2
            i += 1
        else:
            testi = testi / 3
            i += 1
    return i

def divm():
    i = 0
    testi = inputValue - 1
    while testi % 2 == 0 or testi % 3 == 0:
        if testi % 2 == 0:
            testi = testi / 2
            i += 1
        else:
            testi = testi / 3
            i += 1
    return i

def case1():    
    n = 0
    test1 = inputValue
    while not test1 == 1:
        if test1 % 3 == 0:
            n += 1
            test1 = test1 / 3
        elif test1 % 2 == 0 and div() >= divm():
            test1 = test1 / 2
            n += 1
        else:
            test1 -= 1
            n += 1
    return n

def case2():
    n = 0
    test2 = inputValue
    while not test2 == 1:
        if test2 % 3 == 0:
            n += 1
            test2 = test2 / 3
        elif test2 % 2 == 0 and div() > divm():
            test2 = test2 / 2
            n += 1
        else:
            test2 -= 1
            n += 1
    return n

if case1() >= case2():
    print(case2())
else:
    print(case1())
