# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	1024 MB	2597	1644	1557	65.668%
# 문제
# 춘배와 나비, 영철은 어느 날 지구에 나타난 UFO에게 감마선을 맞을 뻔했다. 다행히도 감마선은 행복하게 뒹굴고 있던 고양이들 옆에 있던 컴퓨터에 맞았지만, 이로 인해 컴퓨터에 저장된 춘배와 나비, 영철의 소중한 사진들의 픽셀이 모두 섞이는 사태가 발생했다! 더 이상 형체를 알아볼 수 없게 된 사진들을 보며 슬퍼하던 고양이들은 사진 복구로 유명한 전문가에게 사진의 복구를 맡기기로 했다. 자신의 사진을 다른 고양이가 보는 게 싫었던 춘배는 사진 복구를 맡기기 전에 당신에게 사진을 분류해 주는 프로그램을 만들어 달라고 부탁하였다.

# 프로그램은 주어진 사진이 어떤 고양이의 사진인지 구분해야 한다. 하얀색(w)이 존재한다면 춘배, 검은색(b)이 존재한다면 나비, 회색(g)이 존재한다면 영철의 사진이다. 사진은 고양이(w, b, g) 또는 배경(r, o, y, p)으로 이루어져 있으며 한 사진에 고양이는 무조건 1마리만 나온다.

		
# 춘배(w)	나비(b)	영철(g)
# 입력으로 주어진 사진이 어떤 고양이의 사진인지 구분해 주자.

# 입력
# 15줄에 걸쳐 한 줄에 15개씩 섞여버린 사진의 픽셀 색이 공백으로 구분되어 주어진다.

# 출력
# 춘배의 사진이라면 chunbae, 나비의 사진이라면 nabi, 영철의 사진이라면 yeongcheol을 출력한다.


case1 = "chunbae"
case2 = "nabi"
case3 = "yeongcheol"


set1 = set()

temp = set("1")

while temp:
    try:
        temp = set(map(tuple, input().split()))
    except:
        break
    set1 = set1 | temp




if tuple("w") in set1:
    print(case1)
elif tuple("b") in set1:
    print(case2)
elif tuple("g") in set1:
    print(case3)
else:
    print("?")