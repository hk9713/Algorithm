# 나의 풀이
def solution(n):
    piece = 1
    while True:
        if (n*piece) % 6 == 0:
            return (n*piece)//6
        else:
            piece += 1

# 배운 풀이
import math
def solution(n):
    return (n*6)// math.gcd(n,6) // 6