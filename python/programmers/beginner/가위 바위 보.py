# 나의 풀이
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '0':
            answer += '5'
        elif i == '2':
            answer += '0'
        else:
            answer += '2'
    return answer

# 배운 풀이
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)