# 문제
# Recently, a mathematician has just found three cube numbers that sum up to 42 using over a million hours of computing time. With this breakthrough, we have found three cube numbers that sum up to all non-negative integers less than 100 if it is possible to do so. In other words, for every 0 ≤ N < 100, we have found the triples (X, Y, Z) such that X3 + Y3 + Z3 = N, or we have proved that no such triplet exists.

# The following is a table of (X, Y, Z) that satisfies X3 + Y3 + Z3 = N for 0 ≤ N < 50.

# N	X	Y	Z
# 0	0	0	0
# 1	0	0	1
# 2	0	1	1
# 3	1	1	1
# 4	No solution
# 5	No solution
# 6	-1	-1	2
# 7	0	-1	2
# 8	0	0	2
# 9	0	1	2
# 10	1	1	2
# 11	-2	-2	3
# 12	7	10	-11
# 13	No solution
# 14	No solution
# 15	-1	2	2
# 16	-511	-1609	1626
# 17	1	2	2
# 18	-1	-2	3
# 19	0	-2	3
# 20	1	-2	3
# 21	-11	-14	16
# 22	No solution
# 23	No solution
# 24	-2901096694	-15550555555	15584139827
# 25	-1	-1	3
# 26	0	-1	3
# 27	0	0	3
# 28	0	1	3
# 29	1	1	3
# 30	-283059965	-2218888517	2220422932
# 31	No solution
# 32	No solution
# 33	8866128975287528	-8778405442862239	-2736111468807040
# 34	-1	2	3
# 35	0	2	3
# 36	1	2	3
# 37	0	-3	4
# 38	1	-3	4
# 39	117367	134476	-159380
# 40	No solution
# 41	No solution
# 42	-80538738812075974	80435758145817515	12602123297335631
# 43	2	2	3
# 44	-5	-7	8
# 45	2	-3	4
# 46	-2	3	3
# 47	6	7	-8
# 48	-23	-26	31
# 49	No solution
# Reading a long table is a tedious job, so you would like to create a program that takes N as an input, and produce X, Y, Z as the output. The value of X, Y, and Z must be an integer not less than −1018 and not more than 1018.

# 입력
# Input begins with a line containing an integer: N (0 ≤ N < 50).

# 출력
# Output in a line three integers (separated by a single space): X Y Z that satisfies the condition given in the problem statement. If there is more than one solution, you can output any of them. If there is no solution, output 0 instead.

# 예제 입력 1 
# 2
# 예제 출력 1 
# 3737830626090 1490220318001 -3815176160999
# Other answers such as X = 1214928, Y = 3480205, and Z = −3528875 are also accepted.

# 예제 입력 2 
# 5
# 예제 출력 2 
# 0



ans = '''0	0	0	0
1	0	0	1
2	0	1	1
3	1	1	1
4	No solution
5	No solution
6	-1	-1	2
7	0	-1	2
8	0	0	2
9	0	1	2
10	1	1	2
11	-2	-2	3
12	7	10	-11
13	No solution
14	No solution
15	-1	2	2
16	-511	-1609	1626
17	1	2	2
18	-1	-2	3
19	0	-2	3
20	1	-2	3
21	-11	-14	16
22	No solution
23	No solution
24	-2901096694	-15550555555	15584139827
25	-1	-1	3
26	0	-1	3
27	0	0	3
28	0	1	3
29	1	1	3
30	-283059965	-2218888517	2220422932
31	No solution
32	No solution
33	8866128975287528	-8778405442862239	-2736111468807040
34	-1	2	3
35	0	2	3
36	1	2	3
37	0	-3	4
38	1	-3	4
39	117367	134476	-159380
40	No solution
41	No solution
42	-80538738812075974	80435758145817515	12602123297335631
43	2	2	3
44	-5	-7	8
45	2	-3	4
46	-2	3	3
47	6	7	-8
48	-23	-26	31
49	No solution'''

ans = ans.split("\n")
ans  = [line.split() for line in ans]
#print(ans)

n = input()

for i in ans:
    if i[0] == n:
        if i[1] != "No":
            print(*i[1:], sep = ' ')
        else:
            print(0)
        quit()