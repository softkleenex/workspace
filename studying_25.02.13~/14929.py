import sys
input = sys.stdin.readline

import itertools

n = int(input())

# print(help(itertools.combinations))

nums =(list(map(int, input().split())))

ans1 = (pow(sum(nums) , 2)) 

ans2 = sum(pow(num, 2) for num in nums)


print((ans1 - ans2) // 2)