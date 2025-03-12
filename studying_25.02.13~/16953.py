# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	67519	27986	22026	39.847%
# 문제
# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다. 
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

# 입력
# 첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

# 출력
# A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

def f1(x, y):
    x = x  * 2
    if (x > y):
        return -1
    
    return x

def f2(x, y):
    x = x * 10 + 1
    if (x > y):
        return -1
    
    return x

def ans(a, b, count):
    a1 = f1(a, b)
    a2 = f2(a, b)
    count += 1
    c = 0

    if a1 == -1 and a2 == -1:
        return -1
    if a1 != -1:
        c = ans(a1, b, count)
    if a2 != -1:
        c = ans(a2, b, count) if (ans(a2, b, count) != -1) and (c == -1 or c > ans(a2, b, count)) else c



    if a1 == b or a2 == b:
        return count

    return c


    

a, b = map(int, input().split())

count = 0


answer = ans(a, b, count) + 1 if ans(a, b, count) != -1 else -1
print(answer)