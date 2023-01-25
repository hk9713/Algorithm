# 나의 풀이
def solution(n):
    answer = []
    num = 2
    while num <= n:
        if n % num == 0:
            answer.append(num)
            n = n/num
        else:
            num += 1
    return sorted(list(set(answer)))