# 나의 풀이
def solution(box, n):
    return (box[0]//n) * (box[1]//n) * (box[2]//n)

# 배운 풀이
def solution(box, n):
    x, y, z = box
    return (x // n) * (y // n) * (z // n )