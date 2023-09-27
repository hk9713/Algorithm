# 1193 - 분수찾기
# 1/1 > 1/2 > 2/1 > 3/1 > 2/2 > 1/3 > 1/4...
# 출력 - X번째 분수

X = int(input())

line = 1

while X > line:
    X -= line
    line += 1

if line % 2 != 0:
    up = line - X +1
    down = X
else:
    up = X
    down = line - X +1

print(up, '/' ,down, sep="")
