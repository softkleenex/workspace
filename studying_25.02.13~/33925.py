n, j, s, h, k = map(int, input().split())

map1 = input()
map2 = input()
map3 = input()

totalmap = list(zip((x1 for x1 in map1), (x2 for x2 in map2), (x3 for x3 in map3)))

# print(totalmap)

totalmap2 = [0, 0, 0]

for i, v in enumerate(totalmap):
    if totalmap[i].count('v') == 2:
        totalmap2[0] += 1
    elif totalmap[i].count('^') == 1:
         totalmap2[1] += 1
    elif totalmap[i].count('^') == 2:
         totalmap2[2] += 1



# print(totalmap2)

while s > 0 and totalmap2[0] > 0:
    s -= 1
    totalmap2[0] -= 1


while j > 0 and totalmap2[1] > 0:
    j -= 1
    totalmap2[1] -= 1


while j >= 2 and totalmap2[2] > 0:
    j -= 2
    totalmap2[2] -= 1



# print(totalmap2)


ans = h - sum( [x * k for x in totalmap2 if x >= 0])

print(ans) if ans > 0 else print(-1)
