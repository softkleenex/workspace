n = int(input())

list1 = list(map(int, input().split()))
list2 = [1 for i in range(n)]
list3 = [1 for i in range(n)]


# print(list1)
# print(list2)


for i in range(1, n):
    if  list1[i-1] <= list1[i]:#현재 인덱스가 증가중인 인덱스라면
        list2[i] = list2[i - 1] + 1

for i in range(1, n):
    if  list1[i-1] >= list1[i]:#현재 인덱스가 감소중인 인덱스라면
        list3[i] = list3[i - 1] + 1



# print(list1)
# print(list2)
# print(list3)

print(max(max(list2), max(list3)))