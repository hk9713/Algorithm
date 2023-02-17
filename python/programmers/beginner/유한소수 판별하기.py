# 나의 풀이
import math
def solution(a, b):
    answer = []

    gcd = math.gcd(a,b)
    if gcd != 1:
        b /= gcd
        
    temp = 2
    while temp**2 <= b:
        while b % temp == 0 :
            answer.append(temp)
            b = b // temp
        temp += 1
    if b > 1:
        answer.append(b)
    answer = list(set(answer))
    
    for num in answer:
        if num != 2 and num != 5 :
            return 2
    
    return 1

# 배운 풀이
def solution(a, b):
    b //= math.gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2