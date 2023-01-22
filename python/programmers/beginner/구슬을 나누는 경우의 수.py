# 나의 풀이
import math
def solution(balls, share):
    return math.factorial(balls)/(math.factorial(balls-share)*math.factorial(share))

#  배운 풀이
def solution(balls, share):
    return math.comb(balls, share)