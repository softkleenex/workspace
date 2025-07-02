# 문제
# 도서관에서 어떤 책을 K권 보유하고 있고, 이 책에 대한 대출 관리를 담당하고 있는 관리인이 있다. 이 관리인은 월 별로 한 번씩 대출 요청 건들을 취합하여 처리한다. 한 예약 요청은 대출 날짜와 반납 날짜를 포함한다. 예를 들어 이번 달에 이 관리인 처리할 데이터(대출일, 반납일)는 다음과 같다. 

# (1, 2)
# (3, 6)
# (5, 8)
# 관리자는 이러한 대출 요청 정보를 바탕으로 해당 달의 대출 요청이 모두 수용 가능한지 불가능한지를 판단한다. 예를 들면 K=1일 때, 특정 책을 1권 보유 중이라면, 위와 같은 대출 요청이 들어오면 5일에 발생할 대출 요청이 수용 불가하게 된다. (3일에 대출된 책이 6일이 되어야 반납되기 때문)

# 도서 대출 요청 수용 여부를 판단할 수 있는 프로그램을 작성하시오. 모든 반납이 대출보다 먼저 이루어진다고 가정한다.

# 입력
# 첫째 줄에 대출 요청의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개의 줄에 한 사람의 대출일과 반납일이 주어진다. 반납일은 대출일보다 항상 크며, 모든 날짜는 31보다 작거나 같은 자연수이다.

# 마지막 줄에 책의 개수 K(1 ≤ K ≤ 100)가 주어진다.

# 출력
# 도서 대출 요청이 모두 가능하면 1을 불가능하면 0을 출력한다.

# 예제 입력 1 
# 3
# 1 2
# 3 6
# 5 8
# 1
# 예제 출력 1 
# 0
# 예제 입력 2 
# 3
# 1 2
# 3 4
# 5 8
# 1
# 예제 출력 2 
# 1
# 예제 입력 3 
# 3
# 1 2
# 3 6
# 5 8
# 2
# 예제 출력 3 
# 1


import sys
input = sys.stdin.readline


n = int(input())


list1 = []
list2 = []

for _ in range(0, n):
    a, b = map(int, input().split())
    list1.append(a)
    list2.append(b)
    list1.sort()
    list2.sort()



books = []



while list1 and list2:
    while (list1 and list2) and (list1[0]  <  list2[0]):
        list1.pop(0)
        books.append(-1)

    while (list1 and list2) and (list1[0]  >=  list2[0]):
        list2.pop(0)
        books.append(+1)

if list1:
    for i in list1:
        books.append(-1)
    del list1
elif list2:
    for i in list2:
        books.append(+1)
    del list2




# print(books)


book = int(input())

for i in books:
    book += i
    if book < 0:
        print(0)
        quit()

print(1)