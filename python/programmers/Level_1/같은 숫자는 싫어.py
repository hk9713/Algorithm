# 나의 풀이
def solution(arr):
    answer = []
    for num in arr:
        if len(answer) == 0:
            answer.append(num)
        elif answer[-1] != num:
            answer.append(num)
        else:
            continue
    return answer

# 배운 풀이
def no_continuous(s):
    answer = []
    for num in s:
        if answer[-1:] == [num]: 
            continue
        answer.append(num)
    return answer