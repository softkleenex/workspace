n, m = map(int, (input().split()))

stu = dict((x, set()) for x in range(1, n + 1))






for x in range(m):
    x1, x2 = map(int, input().split())
    stu[x1].add(x2)
    stu[x2].add(x1)


stu = [len(x) for x in stu.values()]


print(*stu, sep = '\n')

