# 문제
# 상근이와 친구들은 MT에 가서 아래 설명과 같이 재미있는 게임을 할 것이다.

# 각 플레이어는 1이상 100 이하의 정수를 카드에 적어 제출한다. 각 플레이어는 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻는다. 만약, 같은 수를 쓴 다른 사람이 있는 경우에는 점수를 얻을 수 없다.

# 상근이와 친구들은 이 게임을 3번 했다. 각 플레이어가 각각 쓴 수가 주어졌을 때, 3번 게임에서 얻은 총 점수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 참가자의 수 N이 주어진다. (2 ≤ N ≤ 200) 둘째 줄부터 N개 줄에는 각 플레이어가 1번째, 2번째, 3번째 게임에서 쓴 수가 공백으로 구분되어 주어진다.

# 출력
# 각 플레이어가 3번의 게임에서 얻은 총 점수를 입력으로 주어진 순서대로 출력한다.

# 예제 입력 1 
# 5
# 100 99 98
# 100 97 92
# 63 89 63
# 99 99 99
# 89 97 98
# 예제 출력 1 
# 0
# 92
# 215
# 198
# 89
# 예제 입력 2 
# 3
# 89 92 77
# 89 92 63
# 89 63 77
# 예제 출력 2 
# 0
# 63
# 63

N = int(input())

scores = []
for i in range(0 , N):
    scores.append(list(map(int,  input().split())))#score 0, 1, 2...각각이 참가자의 점수(3개)를 담은 배열

scores_result = [0] * N

#print(scores, sep = '\n')

for i in range(0, 3):#체크할 배열은 0~2 , 길이
    temp_score = []
    for i2 in range(0, N):
        temp_score.append(scores[i2][i])#i2번쨰 사람의 i번쨰 점수를 temp_score에 추가
    for i3 in range(0, N):
        if temp_score.count(temp_score[i3]) == 1:
            scores_result[i3] += temp_score[i3]

print(*scores_result, sep = '\n')