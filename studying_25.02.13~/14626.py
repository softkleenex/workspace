# https://www.acmicpc.net/problem/14626


# m = 10 - (a+3b+c+3d+e+3f+g+3h+i+3j+k+3l) mod 10
def check (list1):
    a = 0
    for i in range(len(list1)):
        if i % 2 == 0:
            a = a + list1[i] * 1
        else:
            a = a + list1[i] * 3




    if  a % 10 == 0:
        return True
    else:
        return False
    

ans = ' '.join(input()).split()



idx = 0

for i in range(len(ans)):
    if ans[i] == '*':
        idx = i
    else:
        ans[i] = int(ans[i])


# print(ans)
# print(idx)
# print()





for i in range(10):
    ans[idx] = i
    # print(ans)

    if check(ans) == True:
        print(i)


