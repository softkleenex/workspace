 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	512 MB	221	123	99	52.660%
# 문제
# There are $n$ houses along the road where Anya lives, each one is painted in one of $k$ possible colors.

# Anya likes walking along this road, but she doesn't like when two adjacent houses at the road have the same color. She wants to select a long segment of the road such that no two adjacent houses have the same color.

# Help Anya find the longest segment with this property.

# 입력
# The first line contains two integers $n$ and $k$ --- the number of houses and the number of colors ($1 \le n \le 100\,000$, $1 \le k \le 100\,000$).

# The next line contains $n$ integers $a_1, a_2, \ldots, a_n$ --- the colors of the houses along the road ($1 \le a_i \le k$).

# 출력
# Output a single integer --- the maximum number of houses on the road segment having no two adjacent houses of the same color.

# 예제 입력 1 
# 8 3
# 1 2 3 3 2 1 2 2
# 예제 출력 1 
# 4
# 힌트
# In the example, the longest segment without neighboring houses of the same color is from the house 4 to the house 7. The colors of the houses are $[3, 2, 1, 2]$ and its length is 4 houses.

# 출처
# Olympiad > Russian Olympiad in Informatics > Russia Team High School Programming Contest > Russia Team High School Programming Contest 2018 M번

# 알고리즘 분류


k, n = map(int, input().split())

list1 = list(map(int, input().split()))
             
list2 = [1 for i in range(k)]



if k > 1:
    for i in range(1, k):
        if list1[i] != list1[i - 1]:
            list2[i] += list2[i - 1]



print(max(list2))