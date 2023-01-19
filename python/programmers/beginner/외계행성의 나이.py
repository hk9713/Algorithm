# 나의 풀이
def solution(age):
    answer = ''
    code_962 = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e',
                5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
    for num in str(age):
        answer += code_962[int(num)]
    return answer

# 배운 풀이
def solution(age):
    return ''.join([chr(int(i)+97) for i in str(age)])