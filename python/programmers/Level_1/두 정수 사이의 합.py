# 나의 풀이
def solution(a, b):
    min_num, max_num = min(a,b), max(a,b)
    return sum([i for i in range(min_num,max_num+1)])

# 배운 풀이
def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2