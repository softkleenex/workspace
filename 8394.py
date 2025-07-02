# https://www.acmicpc.net/problem/8394


n = int(input())



way = [1, 1, 2, 3, 5]
pre = way[-1]
#4 > 4
#5 > (3) + (5)= 8
# 6 >  
# 7 > 


if n < len(way):
    print((way[n]) % 10)
    exit()

else:
    for x in range(5, n + 1):
        pre = (way[-1] + way[-2]) % 10
        way.append(pre)
        
               
print((way[-1]) % 10)
