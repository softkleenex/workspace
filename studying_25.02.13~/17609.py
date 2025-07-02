# https://www.acmicpc.net/problem/17609


from sys import stdin
input = stdin.readline


def check(x):
    if x == x[::-1]:
        return 0
    
    chance = 1

    l, r = 0, len(x) - 1

    while x[l] == x[r]:
        l += 1
        r -= 1
    else:
        def check2(l, r):
            while l < r:
                if x[l] != x[r]:
                    return 2
                l += 1
                r -= 1
            return 1
        
        return 1 if (check2(l + 1, r) == 1) or ((check2(l, r - 1) == 1)) else 2

            


    return 2



t = int(input())

for _ in range(t):
    x = input().strip()
    print(check(x))