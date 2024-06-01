import random

def simulate_baccarat(start_money, bet_money, goal_money, num_simulations):
    lose_count = 0

    for _ in range(num_simulations):
        money = start_money

        while 0 < money < goal_money:
            # 베팅 금액 조정
            bet_money = min(bet_money, money, goal_money - money)

            # 뱅커에 베팅
            if random.random() < 0.4586:  # 뱅커가 이길 확률
                money += bet_money * 0.95
            else:
                money -= bet_money

        if money <= 0:
            lose_count += 1

    lose_probability = lose_count / num_simulations
    return lose_probability

# 각 경우에 대해 시뮬레이션 실행
print(f'a. 돈을 모두 잃을 확률: {simulate_baccarat(10000, 10000, 20000, 10000):.4f}')
print(f'b. 돈을 모두 잃을 확률: {simulate_baccarat(10000, 10000, 100000, 10000):.4f}')
print(f'c. 돈을 모두 잃을 확률: {simulate_baccarat(1000000, 10000, 2000000, 100):.4f}')
print(f'd. 돈을 모두 잃을 확률: {simulate_baccarat(1000000, 10000, 10000000, 100):.4f}')
