# 나의 풀이
def solution(numbers):
    numbers = sorted(numbers, reverse=True)
    return numbers[0] * numbers[1]

# 배운 풀이
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]