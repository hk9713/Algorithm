# 2869 - 달팽이는 올라가고 싶다
# 높이가 V미터인 나무 막대가 있다
# 낮에 A미터 올라가고, 밤에는 B미터 미끄러진다.
# 출력 - 달팽이가 나무 막대를 모두 올라가는데 걸리는 시간

import math

A, B, V = map(int, input().split())

max_moving = A-B
half_moving = V-A
day = (half_moving/max_moving)

if A >= V:
    print(1)
elif ( day == float(day) and float(day) > 0):
    print(math.ceil(day)+1)
else:
    print(day+1)
