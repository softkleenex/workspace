x = 5000
list1 = map(int, input().split())

for v in list1:
    if v == 1:
        x -= 500
    elif v== 2:
        x -= 800
    elif v == 3:
        x -= 10000
    
print(x)