n = int(input())#물고기의수
c = int(input())#떡밥한개의 가격
fishes = []

for i in range(n):
    #물고기의 먹성 x, 크기 s, 가격 w이
    fish = list(map(int, input().split()))

                    
    fishes.append(fish)

# 낚시 포인트에 남은 떡밥의 개수 t보다 작거나 같은 먹성의 물고기 중 가장 크기가 큰 물고기가 유인된다.
# 유인된 물고기는 자기 먹성 만큼의 떡밥을 먹는다.

#최대 떡밥은 100 * 100


ans = 0

for now in range(0, 100*100 + 1):
    nowfeed = now
    nowfishes = [x for x in fishes]
    nowans = -( now * c)

    #now가 던지는 떡밥
    while any(x[0] <= nowfeed for x in nowfishes ):#남아있는 물고기들중에 유효한 물고기가 있는한 반복

        cangetfishes = [x for x in enumerate(nowfishes) if x[1][0] <= nowfeed]#남은 물고기들중에서 떡밥에 관심있는애들만
        
        getedfish = max(cangetfishes, key = lambda x : x[1][1])#그중에 최대 크기
        nowfeed -= getedfish[1][0]#떡밥을 뺴고
        nowans += getedfish[1][2]#가격을 더하고
        nowfishes.pop(getedfish[0])#nowfishes의 인덱스를 참조하여, 잡은 물고기는 제거한다

    ans = max(ans, nowans)


print(ans)
