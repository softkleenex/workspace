# 광활한 영토가 있다. 이 영토는 xy 평면으로 나타낼 수 있고 정확히 3N개의 말뚝이 박혀 있다. 말뚝은 서로 다른 위치에 박혀 있으며, 세 개의 말뚝이 일직선 상에 있는 경우는 없다.

# N명의 사람이 영토를 나누려고 한다. 그들은 각자 3개의 말뚝을 선택하여 말뚝들을 선분으로 이었을 때 생기는 삼각형의 영역을 각자의 영토로 인정하기로 하였다. 물론 두 사람이 선택한 영토가(경계나 모서리라도) 조금이라도 겹치는 일은 일어나서는 안 된다. 그러나 조건을 만족하면서 서로의 말뚝을 선택하는 일은 똑똑하지 못한 그들에게 상당히 어려운 일이었다. 그렇기에 지나가던 똑똑한 당신에게 이 일을 맡기기로 하였다.

# 입력
# 첫 번째 줄에는 사람들의 수 N (1 ≤ N ≤ 300)이 주어진다.

# 다음 3N줄에는 각 말뚝의 위치를 나타내는 두 정수 x,y (−106 ≤ x,y ≤ 106) 가 공백으로 구분되어 주어진다. 말뚝은 입력 받는 순서대로 1에서 3N까지의 번호가 붙는다.

# 출력
# N개의 줄에 걸쳐서 각 사람이 선택한 세 말뚝의 번호를 공백으로 구분하여 출력한다. (잘 생각해보면 알겠지만 불가능한 경우는 없다.)


import sys
input = sys.stdin.readline

n = int(input())
plies = {}

x = 10 ** (-6)

for i in range(0+1, 3*n + 1):
    temp = list(map(int, (input().split())))
    plies[i] = temp


plies_list = list(plies.items())
#print(plies_list)

plies_list.sort(key = lambda x:  x[1])

ans = [x[0] for x in plies_list]
for i in range (0, len(ans)):
    print(ans[i], end = '')

    if (i+1) %3 != 0 or i == 0:
        print(end = ' ')
    else:
        print()

