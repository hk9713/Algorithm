# 나의 풀이
def solution(n):
    answer = [ int(i) for i in str(n) ]
    answer.reverse()
    return answer

# 배운 풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))