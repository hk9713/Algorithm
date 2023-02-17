# 나의 풀이
def solution(n):
    non_three = [0]*100
    temp = 1
    for i in range(100):
        while temp % 3 == 0 or str(temp).find('3') != -1:
            temp += 1
        non_three[i] = temp
        temp += 1
    return non_three[n-1]

# 배운 풀이
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer