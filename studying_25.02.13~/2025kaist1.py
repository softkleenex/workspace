# def ans(a):

# #끝이 빈칸 인거 a 개
# #끝이 검정인 그룹으로 끝나는거b개
# #끝이 흰색인 그룹으로 c개
# #끝이 검정이지만 성립되지 않는거 d개
# # 끝이 흰색이지만 성립되지 않는거 e개

# #ex 1 [1, 0, 0, 1 , 1 ]

# #2[3, 1, 1] 
# #여기까지는 고정


# #3[8 , 4, 4]

# #4[24, 12, 12]

# #5[72 , 36 , 36] 


# n = int(input())

# inlist = []

# for _ in range(n):
#     inlist.append(int(input()))




# for i in range(n):
#     print(ans(inlist[i]))


MOD = 10**9 + 7
MAX = 1000000

dp = [[0] * 3 for _ in range(MAX + 1)]
prefix = [0] * (MAX + 1)

dp[1][0] = 1
dp[1][1] = 0
dp[1][2] = 0
prefix[1] = 1

for i in range(2, MAX + 1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD
    dp[i][1] = prefix[i-1] % MOD
    dp[i][2] = prefix[i-1] % MOD
    prefix[i] = (prefix[i-1] + dp[i][0]) % MOD

res = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    res[i] = (dp[i][0] + dp[i][1] + dp[i][2]) % MOD


print(*res, sep = '\n')