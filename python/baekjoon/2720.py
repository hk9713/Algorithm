# 2720 - 세탁소 사장 동혁
# 첫째 줄에 테스트 케이스 개수 T가 주어진다.
# 출력 - 거스름돈의 액수가 주어졌을 때, 이를 나타내는 (25c, 10c, 5c, 1c) 동전의 개수

T = int(input())
coin = [25, 10, 5, 1]

for _ in range(T):
    money = int(input())
    for c in coin:
        print(money//c, end=' ')
        money = money%c
