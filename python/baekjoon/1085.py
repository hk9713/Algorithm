# 1085 - 직사각형에서 탈출
# 첫째 줄에 x, y, w, h가 주어진다.
# 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)인 직사각형
# 출력 - (x,y)에서 직사각형의 경계선까지 가는 거리의 최솟값

x, y, w, h = map(int,input().split())

width = x if (x < w-x) else (w-x)
height = y if (y < h-y) else (h-y)

print( width if width < height else height)
