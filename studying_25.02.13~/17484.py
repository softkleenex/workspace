# https://www.acmicpc.net/problem/17484

list1 =[]

n, m = map(int, input().split())

for _ in range(n):
    list1.append(list(map(int,input().split())))



list2 = []
for _ in range(n):
    list2.append([0 for i in range(m)])


print(*list1, sep = '\n')
print()
print(*list2, sep = '\n')


#1 왼아래 2 아래 3 오아래 -1 무의미









for i in range(len(list2)):
    for i2 in range(len(list2[0])):
        if i == 0:#가장 첫 행은 시작지점이므로 
            list2[i][i2] = [list1[i][i2], [[i+1, i2], [i+1, i2 + 1], [i+1, i2 - 1] ] ]
        else:
            ables = 100 + 1

            for i3 in range(len(list2[i-1])):
                if [i, i2] in list2[i-1][i3]:
                    ables = min(ables, list2[i-1][i3])


