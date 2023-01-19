# 나의 풀이
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i != 0:
            continue
        answer+=1
    return answer

# 배운 풀이
def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))