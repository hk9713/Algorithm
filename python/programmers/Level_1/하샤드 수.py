# 나의 풀이
def solution(x):
    hap = sum(map(int,[i for i in str(x)]))
    return x % hap == 0

# 배운 풀이
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0