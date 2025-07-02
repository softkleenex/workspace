# 장로는 잠이 바로든다, 특히 s + 0.5초 이상이 어꺠를 두드린이후에 있었다면, 잠이 바로든다. 현재는 깨있고, 어꺠는 두드렸던상태(0초)
# n번 두드린다,. ti초 이후
# 장로가 tn초 이후 꺠있는가?

n, s = map(int, input().split())
tlist = list(map(int, input().split()))




#

if float(tlist[-1] - tlist[-2])  <= s + 0.5:
    print('Yes')
else:
    print('No')