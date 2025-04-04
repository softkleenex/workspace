# 문제
# 국렬이는 모르고리즘 차기 회장을 빠르게 구해야 한다. 안 그러면 대학원 가서도 회장을 해야 하기 때문이다.

# 그래서 국렬이는 어떻게든 2020년 연세대학교 프로그래밍 경진대회를 열어서 차기 회장을 선택하려고 했으나, 코로나19 때문에 미루고 결국 11월에 개최하게 되었다.

# 국렬이는 대회를 치른 사람 중에서 점수가 가장 높은 사람을 억지로 차기 회장으로 지목하려고 한다. 만약에 가장 높은 사람이 2명 이상 있는 경우, 이름이 사전 순으로 가장 앞선 사람을 차기 회장으로 뽑을 것이다.

# 차기 회장으로 누가 지목될지 알아내라.

# 입력
# 다음과 같이 입력이 주어진다.

# N
# A1 B1
# . . . . . .
# AN BN
# 출력
# 첫째 줄에 차기 회장으로 뽑힐 사람의 이름을 출력하여라.

# 제한
# 1 ≤ N ≤ 100,000. N은 사람의 수를 나타내는 양의 정수다.
# Ai는 길이가 1 이상 10 이하의 알파벳 소문자로 구성된 문자열로 참여자의 이름이다. (1 ≤ i ≤ N)
# Ai ≠ Aj (1 ≤ i < j ≤ N)
# 1 ≤ Bi ≤ 1,000,000,000 (1 ≤ i ≤ N). Bi는 점수를 의미하는 양의 정수다.
# 예제 입력 1 
# 3
# inseop 10
# gukryeol 1
# juno 11
# 예제 출력 1 
# juno
# 예제 입력 2 
# 3
# inseop 10
# gukryeol 10
# juno 10
# 예제 출력 2 
# gukryeol

import sys
input = sys.stdin.readline

n = int(input())

players_scores = list()

for _ in range(0, n):
    player, score = input().split()
    score = int(score)
    players_scores.append([score, player])


players_scores.sort(key = lambda i: i[1])   
players_scores.sort(key = lambda i: i[0], reverse = True)   


print(players_scores[0][1])