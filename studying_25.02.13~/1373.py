# 	128 MB	37776	15093	12485	41.362%
# 문제
# 2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 2진수가 주어진다. 주어지는 수의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 주어진 수를 8진수로 변환하여 출력한다.



x = int(input(), 2)

print(oct(x)[2:])
