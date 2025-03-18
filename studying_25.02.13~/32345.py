# 홍익대학교의 영어 이름은 hongik university이다. 하지만 읽는 사람에 따라 이를 hong/ik으로 발음하지 않고, hon/gik으로 발음해 혼긱대학교가 되는 웃지 못할 상황이 종종 벌어지곤 한다.

# 자음이 앞 모음에 붙느냐, 뒤 모음에 붙느냐에 따라 단어의 발음이 다른 것을 신기하게 여긴 동현이는 비슷한 상황인 영어 단어들을 조사해서 발음이 얼마나 다양하게 될 수 있는지를 알아보려 한다. 하지만, 영어를 잘 못하는 동현이는 아래의 규칙에 따라서만 발음을 파악한다.

# 영어 모음은 a, e, i, o, u 5개이며, 자음은 모음을 제외한 나머지 21개의 알파벳이다.
# 1개의 모음에 0개 이상의 자음이 앞뒤로 붙어서 하나의 음이 되고, 음들이 모여서 단어의 발음이 된다.
# 예) h, o, n, g, i, k → hong, ik → hongik
# 자음과 자음, 자음과 모음은 인접했을 때만 한 음으로 모일 수 있다.
# 음에 구성된 알파벳의 개수, 구성, 순서가 다른 경우 다른 음으로 취급한다.
# 예) ab와 abb, ba는 모두 다른 음이다.
# 주어진 단어의 알파벳을 각각 1회씩 사용해서 발음을 만들어야 한다.
# 각 음의 구성이 다른 경우 단어의 발음이 다른 것으로 생각한다.
# 이와 같은 규칙에 따라 단어들이 발음될 수 있는 경우의 수를 출력해 보자.

# 입력
# 첫째 줄에 테스트 케이스의 개수 
# \(T\)가 주어진다. 
# \((1 ≤ T ≤ 100\,000)\) 

# 둘째 줄부터 
# \(T\)개의 줄에 걸쳐, 알파벳 소문자로 이루어진 단어 
# \(S\)가 주어진다. 
# \((1 ≤ |S| ≤ 300\,000)\) 

# 모든 테스트 케이스에 대해 단어의 길이의 합은 
# \(1\,000\,000\) 이하이다.

# 출력
# 매 줄마다, 각 테스트 케이스에서 단어의 발음의 경우의 수를 출력한다.

import string
import math
import sys

input = sys.stdin.readline
alpha = set(string.ascii_lowercase)


vowel = set(['a', 'e', 'i', 'o', 'u'])#모
consonant = alpha - vowel#자

#print(vowel, consonant)

t = int(input())

for _ in range(0, t):
    target = (' '.join(input())).split()
    if all( (   not(temp in vowel) for temp in target   )   ):
        print('-1')
        continue

    #print(target)
    ans = 1
    count = 1
    #step1. 양끝의 자음은 가장 가까운 모음에 붙을 수 밖에 없으므로 제거한다
    while target[0] in consonant:
        #print(target[0])
        target.pop(0)
    while target[len(target) -1] in consonant:
        #print(target[0])
        target.pop()

    #print(target)
    #step2. 모 ~ 자1 ~ 모 ~ 자2 ~.... ~모 의 꼴일텐데, 자의 입장에서는 그들 사이에 구분할 / 를 넣는것과 같은 케이스 아닌가?
    #자음이 x개 있다고 하면, / 를 넣을수 있는 공간은 x + 1, 즉, 자음들 각 공간의 + 1 의 누적곱? > 파이?
    #예시 1 > 3, 예시 2 > 2,, 맞는듯?

    for i in target:
        if i in vowel:
            if count != 1:
                ans = (ans * count)%(math.pow(10, 9) + 7)
                count = 1
        elif i in consonant:
            count += 1

    #시간초과, 현재 target 은 양끝이 손질된 상태이므로, 자음으로 만들어진 리스트 모음을 만드는 방식은 어떤가? > 어떻게? o(len(t))도 시간초과 나는 마당에?
    print(int(ans))