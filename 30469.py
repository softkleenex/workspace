a, b, n = map(int, input().split())

if (b // 10) % 2  == 0 or (b // 10)  == 5:
    print(-1)
    exit()

print(a, end = '')
if a % 10 == 9:
    print(71, end = '')
else:
    print(11, end = '')

print(* ([1] * (n - 6)), sep = '', end = '')
print(b)