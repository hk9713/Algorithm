# 2563 - 색종이
# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.
# 이 도화지 위에 가로, 세로의 크기가 10인 정사각형 모양의 검은색 색종이를 한 장 또는 여러 장 붙인다.
# 첫 줄에는 색종이의 수가 주어진다.
# 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다.
# 출력 - 색종이가 붙은 검은 영역의 넓이

paper = [ [ 0 for _ in range(100)] for _ in range(100) ]

cnt = int(input())
for _ in range(cnt):
    x, y = map(int, input().split())
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            paper[i][j] = 1

answer = 0
for list in paper:
    answer += list.count(1)

print(answer)
