a = input().strip()
b = input().strip()




for i in range(len(b)):
    if not(b[i] in a): 
        print(b[i], end = '')