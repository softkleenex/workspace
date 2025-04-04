# 문제
# 라그랑주는 1770년에 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다고 증명하였다. 
# 어떤 자연수는 복수의 방법으로 표현된다. 예를 들면, 26은 52과 12의 합이다; 
# 또한 42 + 32 + 12으로 표현할 수도 있다. 역사적으로 암산의 명수들에게 공통적으로 주어지는 문제가 바로 자연수를 넷 혹은 그 이하의 제곱수 합으로 나타내라는 것이었다. 1900년대 초반에 한 암산가가 15663 = 1252 + 62 + 12 + 12라는 해를 구하는데 8초가 걸렸다는 보고가 있다. 좀 더 어려운 문제에 대해서는 56초가 걸렸다: 11339 = 1052 + 152 + 82 + 52.

# 자연수 n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램을 작성하시오.

# 입력
# 입력은 표준입력을 사용한다. 입력은 자연수 n을 포함하는 한 줄로 구성된다. 여기서, 1 ≤ n ≤ 50,000이다.

# 출력
# 출력은 표준출력을 사용한다. 합이 n과 같게 되는 제곱수들의 최소 개수를 한 줄에 출력한다.

n = int(input())

ans = [1, 1, 2, 3, 1, 2]
for i in range(len(ans), n + 1):
    temp_min = 4
    if (i**(1/2)).is_integer():
        temp_min = 1
    else:
        for i2 in range(int(i**(1/2)), 0, -1):
            temp_min = temp_min if ((ans[i2 ** 2] + ans[i - i2**2]) > temp_min) else ans[i2 ** 2] + ans[i - i2**2]
        # while move < now - move:
        #     #print(move, now)
        #     temp_min = temp_min if temp_min < ans[move] + ans[now - move] else ans[move] + ans[now - move]
        #     move += 1
        #비요율적, 제곱수가 있는 경우만 체크해

    ans.append(temp_min)

print(ans[n])
    