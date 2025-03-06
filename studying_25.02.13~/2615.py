# ISIS Puzzle은 "Identify, Sort, Index, Solve"의 절차로 푸는 퍼즐을 통칭한다.

# 퍼즐을 좋아하는 하이비는 HCPC에 아래와 같은 ISIS 퍼즐 문제를 내기로 했다.

#  
# $ N $개의 문자열 
# $ S_1, S_2, \ldots, S_N $이 주어진다.
# Identify: 각 문자열과 대응되는 문제의 제목을 알아낸 뒤, 그 문제의 번호 
# $ I_i $와 난이도 
# $ D_i $를 알아낸다.
# Sort: 문제들을 번호 
# $ I_i $의 오름차순으로 정렬한다.
# Index: 각 문제 이름 
# $ S_i $에서 
# $ D_i $번째의 글자를 추출한다. 이때 추출된 글자가 소문자라면 대문자로 변환한다.
# Solve: Index 단계에서 추출한 글자들을 Sort 단계에서 정렬한 순서대로 나열한다.
# 하지만 Identify는 구현이 어려울 것이라고 생각해, Identify까지 완료된 자료를 주기로 했다.

# Identify가 완료된 자료가 주어질 때, Sort, Index, Solve까지 완료한 뒤 나오는 문자열을 출력해보자.

# 입력
# 첫째 줄에는 자료의 수 
# $ N $이 주어진다. 
# $( 1 \le N \le 100 )$ 

# 둘째 줄부터 
# $ N $개의 줄에 걸쳐서 문제 제목 
# $ S_i $, 번호 
# $ I_i $, 난이도 
# $ D_i $가 주어진다. 
# $( 1 \le |S_i| \le 100; $ 
# $ 1 \le I_i \le 100\,000; $ 
# $ 1 \le D_i \le |S_i| )$ 

#  
# $ S_i $는 알파벳 대소문자와 숫자로만 이루어져 있다.

# 두 문제가 동일한 번호를 가지고 있는 경우는 없다.

import sys
input = sys.stdin.readline

list1 = []

n = int(input())

for i in range(0, n):
    temp = input().split()
    temp[1], temp[2] = map(int, (temp[1], temp[2]))
    list1.append(temp)

list1.sort(key = lambda x : x[1])

#print(list1)

for i in range(0, len(list1)):
    list1[i][0] = (''.join(list1[i][0])[list1[i][2] - 1])
    list1[i][0] = list1[i][0].upper()


list2 = list(zip(*list1))
print(*list2[0], sep ='')