# 나의 풀이
def solution(num_list, n):
    answer = []
    temp = []
    for num in num_list:
        temp.append(num)
        if len(temp) == n:
            answer.append(temp)
            temp = []
    return answer

# 배운 풀이
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer