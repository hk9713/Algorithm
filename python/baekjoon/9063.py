# 9063 - 대지
# 첫 번째 줄에 점의 개수 N (1 ≤ N ≤ 100,000) 이 주어진다.
# 이어지는 N 줄에는 각 점의 좌표가 두 개의 정수로 한 줄에 하나씩 주어진다.
# 출력 - N 개의 점을 둘러싸는 최소 크기의 직사각형의 넓이

x_list = []
y_list = []

N = int(input())

if N < 2:
    print(0)

else:
    for _ in range(N):
        x, y = map(int, input().split() )
        x_list.append(x)
        y_list.append(y)

    print( (max(x_list)-min(x_list))*(max(y_list)-min(y_list)) )
