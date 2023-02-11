# 나의 풀이
def solution(n):
    return sum([i for i in range(1, n+1) if (n/i).is_integer()])

# 배운 풀이
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상됨
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])