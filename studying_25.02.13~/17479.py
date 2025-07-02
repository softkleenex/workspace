# https://www.acmicpc.net/problem/17479

from sys import stdin
input = stdin.readline

a, b, c = map(int, input().split())

normal = dict()
special = dict()
service = set()

for _ in range(a):
    name, cost = input().split()
    normal[name]  = int(cost)



for _ in range(b):
    name, cost = input().split()
    special[name]  = int(cost)


for _ in range(c):
    name = input().strip()
    service.add(name)





n = int(input())
order = list()


for _ in range(n):
    order.append(input().strip())


normalc = 0
specialc = 0
servicec = 0

for x in order:
    if x in normal:
        normalc += normal[x]
    elif x in special:
        specialc += special[x]
    elif x in service:
       servicec += 1
    else:
        print(x, 'error')


# 특별메뉴는 일반메뉴에서 총 20,000원 이상을 주문해야 주문할 수 있다.
# 서비스메뉴는 일반메뉴와 특별메뉴에서 총 50,000원 이상을 주문해야 주문할 수 있다.
# 서비스메뉴는 단 하나만 주문할 수 있다.

# print(normalc, specialc, servicec)

if specialc > 0:
    if not (normalc >= 20000):
        print("No")
        exit()



if servicec == 1:
    if not (normalc + specialc) >= 50000:
        print("No")
        exit()

if servicec > 1:
    print("No")
    exit()

print("Okay")


