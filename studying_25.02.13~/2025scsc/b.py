#0층에는 0개의 주사위가 0개의 면
#1층에는 (0 + 1) 1개의 주사위가 5개의면 > [0, 0, 0, 0, 0, 1]
#2층에는 5개의 면 + (1 + 2) 3개의 주사위가 4 * 2 + 2 * 1 = 10, 총 15개의 면 > [0, 0, 1, 0, 2, 1]
#3층에 15개의 면 + (3 + 3) 6개의 주사위가 4 * 2 + (3 * 1 + 1 * 2) + 2 * 1 = 15, 총 30개의 면 >[0, 2, 2, 1, 4, 1]
#4층에는 30개의 면 + (6 +4) 10개의 주사위가 4 * 2 + (3 * 2 + 1 * 4) + 2 * 1 + (0 * 1) = 50개의면
#5층에는            (10 + 5)15개의 주사위가 4 * 2 + (3 * 3 + 1 * 8) + 2 * 1  + (0 * 1) = 






ans = [[0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 2, 1]]


a = int(input())





if a >= 3:
    for i in range(3, a + 1):#현재 i 층 탐색중
        temp = [x for x in ans[-1]]
        temp[4] += 2
        temp[3] += (i - 2)
        temp[2] += 1
        temp[1] += pow(2, i - 2)
        ans.append(temp)


# print(1 + 2 + 3 + 4 + 5 + 6) = 21


def maxdice(dices):
    dice = [0, 6, 11, 15, 18, 20] 
    ansmax = [v * dice[i] for i, v in enumerate(dices)]
    return(sum(ansmax))

def mindice(dices):
    dice = [0, 1, 3, 6, 10, 15] 
    ansmin = [v * dice[i] for i, v in enumerate(dices)]

    return(sum(ansmin))



for i in range(len(ans)):
    print(i, ans[i])

print(maxdice(ans[-1]) + mindice(ans[-1]))