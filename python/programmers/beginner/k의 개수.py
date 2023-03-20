# 나의 풀이
def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        answer += str(num).count(str(k))
    return answer

# 배운 풀이
def solution(i, j, k):
    answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer