import math


def IsPrime(x):#x는 두자릿수, 2 이상, x미만중에서 나누어 떨어지는 수가 있으면 아뇜
    if x < 2:
        return False
    for x2 in range(2, int(x**0.5) + 1):
        if x % x2 == 0:
            return False
        
    return True

a, b, n = map(int, input().split())
#a, b, 는 소수임!!

#2, 8 인 경우는 없으니(A는 소수니까,, 다 1로 채우면 될듯?)

# ans = [a // 10] + [a % 10]  + [1]* (n - 4) + [b // 10] + [b % 10]

# print(ans)
#01 은 소수가 아니라고 치는듯?

ans = [a]
pre = int(ans[-1])

for x in range(n- 4):
    for x2 in range(0, 9 + 1):
        if IsPrime(int(pre)* 10 + int(x2)):
            ans += [x2]
            pre = ans[-1]
            break
        if x2 == 9:
            print(-1)
            exit()

if not IsPrime(pre * 10 + b // 10):
    print(-1)
    exit()
        
print(*ans, b, sep = '')