# 나의 풀이
def solution(n):
    answer = 1
    while answer < n:
        if n % answer == 1:
            return answer
        answer += 1

# 배운 풀이
def solution(n):
    return [next(x for x in range(1,n+1) if n%x==1)][0]