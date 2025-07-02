# [ 1 [ 2 3 ] foo [ 7 bar ] [ ] [ [ ] ] ]
# [] 쌍 6개 6 * 8 = 48
# 정수 4개 8 * 4 = 32 # type: ignore
# 문자열 foo bar, 12 + 3, 12 + 3 = 30

# 110

list1 = input().split()

list1.sort()

# print(list1, sep = '\n')

number = 0
spell = 0
partition = 0



for i in list1:
    try:
        if type(int(i)) == type(1):
            number += 1 * 8

    except:
        if i == '[' or i == ']':
            partition += 1 * 8
        else:
            spell += len(i) + 12


# print(number, spell, partition// 2)

print(sum([number, spell, partition//2]))