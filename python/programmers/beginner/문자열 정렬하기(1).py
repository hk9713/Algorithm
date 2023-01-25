# 나의 풀이
import re
def solution(my_string):
    answer = []
    for char in my_string:
        if char.isdigit():
            answer.append(int(char))
    return sorted(answer)

# 배운 풀이
def solution(my_string):
    return sorted(map(int, (list(re.sub('[^0-9]','', my_string)))))