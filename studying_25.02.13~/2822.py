list1 = []

for i in range(8):
    list1.append([int(input()), i + 1])

# print(list1)

list1.sort(reverse = True)
# print(list1)

# print(list1[:5])

ans1 = sum([i[0] for i in list1[:5]])

ans2 =[i[1] for i in list1[:5]]
ans2.sort()

print(ans1)
print(*ans2)