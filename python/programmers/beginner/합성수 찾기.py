# 나의 풀이
def solution(n):
    answer = 0
    for i in range(1, n+1):
        temp = 0
        for num in range(1, i+1):
            if i % num == 0:
                temp += 1
        if temp >= 3 :
            answer += 1 
    return answer

# 배운 풀이
def solution(n):
    answer = 0
    for i in range(4, n + 1):
        for num in range(2, int(i ** 0.5) + 1):
            if i % num == 0:
                answer += 1
                break
    return  answer