# 나의 풀이
def solution(n):
    return [i for i in range(1, n+1) if n % i == 0]

# 배운 풀이
def solution(n):
    return [i for i in range(1, n+1) if (n/i).is_integer()]