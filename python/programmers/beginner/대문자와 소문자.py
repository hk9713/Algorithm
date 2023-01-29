# 나의 풀이
def solution(my_string):
    answer = ''
    for s in my_string:
        if s.isupper() == True:
            answer += s.lower()
        else:
            answer += s.upper()
    return answer

# 배운 풀이
def solution(my_string):
    return my_string.swapcase()

## str.swapcase() - 대문자와 소문자의 문자열을 변환한다