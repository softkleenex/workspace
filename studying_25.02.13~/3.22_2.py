# 와니는 운동장에서 슛 연습을 하려고 합니다. 운동장은 $A,$ $B,$ $C,$ $D$의 좌표가 각각 $(0,0),$ $(W,0),$ $(W,H),$ $(0,H)$인 직사각형 $ABCD$로 표현할 수 있습니다. $AB$는 운동장의 아래쪽 변, $CD$는 위쪽 변입니다. 슛 연습을 하려면 골대도 필요합니다. 와니는 운동장 내부에 있는 서로 다른 두 점 $P(x_1,y_1),$ $Q(x_2,y_2)$을 고르고, 이 두 점을 양 끝으로 하는 골대를 설치했습니다. 이 때 선분 $PQ$와 변 $AB$는 평행합니다.

# 와니는 운동장 내부의 특정 위치 $(x, y)$에서 공을 찹니다. 와니가 찬 공은 선분 $AB$ 내의 모든 위치에서 균등한 확률로 선택된 한 점을 향해 직선으로 굴러가며, 공이 굴러가다가 중간에 멈추는 경우는 없습니다. 와니가 찬 공의 궤적이 선분 $PQ$와 교차하는 경우, 공이 골대에 들어갔다고 간주합니다.

# 운동장의 크기와 와니의 위치, 골대의 양 끝점 $P,Q$의 위치가 주어질 때, 와니가 공을 찼을 때 공이 골대에 들어갈 확률을 계산하세요.

# 입력
# 첫 번째 줄에 운동장의 가로 길이와 세로 길이를 나타내는 두 정수 $W, H$가 공백을 간격으로 주어집니다. $(1\le W,H\le 30)$ 

# 두 번째 줄에 와니의 위치를 나타내는 두 정수 $x, y$가 공백을 간격으로 주어집니다. $(0 \leq x \leq W;$ $0 \leq y \leq H)$ 

# 세 번째 줄에 점 $P$와 점 $Q$의 위치를 나타내는 네 정수 $x_1, y_1, x_2, y_2$가 공백을 간격으로 주어집니다. $(0 \leq x_1 < x_2 \leq W;$ $0 \leq y_1 = y_2 \leq H;$ $y\neq y_1;$ 니가 공을 찼을 때, 공이 골대에 들어갈 확률을 실수 형태로 출력해 주세요. 정답과의 절대 오차 또는 상대 오차가 $10^{-6}$ 이하인 경우 정답으로 인정됩니다.

w, h = map(int, input().split())
a, b = map(int, input().split())
px, py, qx, qy = map(int, input().split())

c = qy

if(c > b):
    print(0.0)
    quit(0)


t1 = c * (a / b)
t2 = ( c  * ((a - w) / b)) + w 
ans1 = t2 - t1
ans2 = min(qx, t2) - max(px, t1)


#print(t2, t1, ans1, ans2)


print(float(ans2 / ans1) if float(ans2 / ans1)  >= 0 else 0.0)