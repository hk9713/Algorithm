# 나의 풀이
def solution(n):
    answer = 0
    for i in range(n+1):
        if i%2 != 0:
            continue
        answer += i
    return answer

# 배운 풀이
def solution(n):
    return sum([i for i in range(2, n + 1, 2)])