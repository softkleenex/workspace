# 문제
# Given the amount of a purchase (1 ≤ P ≤ 99) in cents, determine the way to make "change for a dollar" for that purchase. Use four standard US coin denominations: 1, 5, 10, and 25. The way to make change uses the least number coins.

# 입력
# A single line with one integer, P, the amount of the purchase.

# 출력
# A single line with four integers telling respectively how many 25 cent, 10 cent, 5 cent, and 1 cent pieces to give as change.

# 예제 입력 1 
# 43
# 예제 출력 1 
# 2 0 1 2


p = 100 - int(input())



ans = p // 25
p = p - ans * 25
print(ans, end = ' ')

ans = p // 10
p = p - ans * 10
print(ans, end = ' ')

ans = p // 5
p = p - ans * 5
print(ans, end = ' ')
ans = p // 1
p = p - ans * 1
print(ans, end = ' ')
