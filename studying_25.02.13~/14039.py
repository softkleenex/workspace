# Magic Squares are square arrays of numbers that have the interesting property that the numbers in each column, and in each row, all add up to the same total.

# Given a 4 × 4 square of numbers, determine if it is magic square.

# 입력
# The input consists of four lines, each line having 4 space-separated integers.

# 출력
# Output either magic if the input is a magic square, or not magic if the input is not a magic square.


m = "magic"
nm = "not magic"

a = [[0 for _ in range(0, 4)] for __ in range(0, 4)]

# print(*a, sep = '\n')

for i in range(0 , 4):
    a[i] = list(map(int, input().split()))

t = int(sum(a[0]))


for i in range(0, 4):
    if t != sum(a[i]):
        print(nm)
        quit()


for i in range(0, 4):
    s = 0
    for i2 in range(0, 4):
        s += a[i2][i]
    if s != t:
        #print(i, i2)
        print(nm)
        quit

print(m)