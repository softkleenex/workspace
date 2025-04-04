# 문제
# An anagram of a string is formed by rearranging the letters in the string. For example, the anagrams of aab are aab, aba, and baa.

# A wildcard anagram of a string is an anagram of the string where some of the letters might have been replaced with an asterisk (*). For example, two possible wildcard anagrams of aab are *ab and *b*.

# Given two strings, determine whether the second string is a wildcard anagram of the first string.

# 입력
# The two lines of input will both consist of N (1 ≤ N ≤ 100) characters. Each character in the first line will be a lowercase letter. Each character in the second line will be either a lowercase letter or an asterisk.

# 출력
# Output the character A if the string on the second line is a wildcard anagram of the string on the first line. Otherwise, output the character N.

# 예제 입력 1 
# abba
# baaa
# 예제 출력 1 
# N
# 예제 입력 2 
# cccrocks
# socc*rk*
# 예제 출력 2 
# A


import collections

in1 = sorted(input())
in2 = sorted(input())

c1 = collections.Counter(in1)
c2 = collections.Counter(in2)

wild = c2['*']
#del c2['*']

dif = c1 - c2

needed = sum(dif.values())

print('A' if needed <= wild else 'N')