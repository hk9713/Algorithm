# 3009 - 네 번째 점
# 세 점의 좌표가 한 줄에 하나씩 주어진다.
# 출력 - 직사각형을 만들기 위해 필요한 네 번째 점

x = []
y = []

for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

dot_x = x[2] if (x[0]==x[1]) else x[0]
dot_y = y[2] if (y[0]==y[1]) else y[0]

print(dot_x, dot_y)
