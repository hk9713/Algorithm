# 나의 풀이
import math
def solution(n):
    answer = 1
    while True:
        if math.factorial(answer) > n :
            return answer - 1
        answer += 1

# 배운 풀이
from math import factorial
def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k