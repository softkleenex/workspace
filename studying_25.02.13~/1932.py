# https://www.acmicpc.net/problem/1932



n = int(input())

pyramid = list()

for _ in range(n):
    temp = list(map(int, input().split()))
    pyramid.append(temp)





# print(*pyramid, sep = '\n')


for i in range(1, len(pyramid)):
    for i2 in range(len(pyramid[i])):
        temp = pyramid[i][i2]
        if 0 <= i2 < len(pyramid[i - 1]):
            temp = max(pyramid[i-1][i2]+ pyramid[i][i2], pyramid[i][i2])

            
        if 0 <= i2 - 1 < len(pyramid[i - 1]):
           temp = max(pyramid[i-1][i2 - 1]+ pyramid[i][i2], temp)
       
        
        pyramid[i][i2] = temp

print(max(pyramid[-1]))