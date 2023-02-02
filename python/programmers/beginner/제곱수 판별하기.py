# 나의 풀이
import math
def solution(n):
    return 1 if math.sqrt(n).is_integer() else 2

# 배운 풀이
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2