import math

b, c, a1, a2 = map(int, input().split())

print((b + math.sqrt(pow(b, 2) + (4 * c))) / 2)