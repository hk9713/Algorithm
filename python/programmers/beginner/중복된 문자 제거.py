# 나의 풀이
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer

# 배운 풀이
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))