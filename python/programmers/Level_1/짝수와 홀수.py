# 나의 풀이
def solution(num):
    return "Even" if num % 2 == 0 else "Odd"

# 배운 풀이
def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]