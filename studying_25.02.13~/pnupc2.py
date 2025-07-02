import sys
input = sys.stdin.readline

n, t = map(int, input().split())

list1 = list(map(int, input().split()))



sortedlist1 = sorted(list1[0 : t])


list1 = list1[t:]


print(*sortedlist1, *list1)

