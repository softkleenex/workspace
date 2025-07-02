import collections

a = int(input())
# a = [int(i) for i in str(a)]
# print(a)

b = input()
b = collections.deque(int(i) for i in str(b))
# print(*b, sep = '\n')


ans = []
for i in reversed(b):
    ans.append(a * i)


ans.append(
    sum([ans[i] * pow(10, i) for i in range(len(ans))]
                                            ))

print(*ans, sep = '\n')