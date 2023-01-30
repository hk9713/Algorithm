# 나의 풀이
def solution(cipher, code):
    answer = ''
    num = code-1
    for i,alphabet in enumerate(cipher):
        if i == num:
            answer += alphabet
            num += code
    return answer

# 배운 풀이
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer