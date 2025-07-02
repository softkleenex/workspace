from math import ceil

n = int(input())
nums = [int(input()) for _ in range(n)]








for num in nums:
    record = []
    for x in range(2, num + 1):
        target = num
        ans = 0
        if num % x == 0 and all((x  % recordnum) != 0 for recordnum in record):
            record.append(x)
            while target % x == 0:
                ans += 1
                target = target // x

            # print(record)
            print(x, ans)