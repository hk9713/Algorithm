# 나의 풀이
def solution(n):
    return (n**0.5 + 1)**2 if (n**0.5).is_integer() else -1

# 배운 풀이
def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or -1