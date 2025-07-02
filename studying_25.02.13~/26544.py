# # 문제
# # Your next-door neighbor has asked to borrow some fencing to put around all of his land. Being the kind neighbor that you are, you’ve decided to lend him your fencing. But being the stingy farmer that you are, you’ve also decided to give him exactly enough, and no more. An interesting quality of your neighbor’s farm is that it’s shaped like a histogram. Given the width and height of each column of the histogram, determine the perimeter of your neighbor’s land.

# # 입력
# # The first line will contain a single integer n that indicates the number of data sets that follow. Each data set will start with a single integer x denoting the number of ‘bars’ in your neighbor’s histogram shaped plot of land. The next two lines consists of x space separated integers each, representing the widths and heights respectively of each bar of land.

# # 출력
# # For each test case, output the amount of fencing needed to surround the perimeter of your neighbors histogram shaped plot of land.

# 예제 입력 1 
# 2
# 7
# 1 1 1 1 1 1 1
# 1 3 6 3 3 3 2
# 3
# 1 2 3
# 1 2 3
# 예제 출력 1 
# 26
# 18

n = int(input())

for _ in range(0, n):
    x = int(input())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))

 
   
    ans = sum(list1) * 2
    
    list3 = list2[0] +  list2[-1]

    for idx  in range(1, len(list2)):
        temp = list2[idx] - list2[idx - 1]

        # print(list2[idx -1])
        # print(list2[idx])


        temp = temp if temp > 0 else -temp
        list3 += temp
    

    
    # print(ans)
    # print(list3)
    ans += list3

    print(ans)