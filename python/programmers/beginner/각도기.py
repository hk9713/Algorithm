# 나의 풀이
def solution(angle):
    if angle == 180:
        return 4
    elif angle > 90:
        return 3
    elif angle == 90:
        return 2
    else:
        return 1

# 배운 풀이
def solution(angle):
    angles = {180: 4, 91: 3, 90: 2, 0: 1}
    for base, result in angles.items():
        if angle >= base:
            return result