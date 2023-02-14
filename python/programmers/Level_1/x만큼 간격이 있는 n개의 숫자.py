# 나의 풀이
def solution(x, n):
    return [ x*i for i in range(1,n+1) ]

# 배운 풀이
def number_generator(x, n):
    return [i for i in range(x, x*n+1, x)]