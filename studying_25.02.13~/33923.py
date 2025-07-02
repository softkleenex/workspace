n, m = map(int, input().split())

if n != m:
    x = min(n, m) - 1
    print(pow(x, 2))
elif n == m:
    temp = pow(n - 2, 2) + 1
    print(temp)