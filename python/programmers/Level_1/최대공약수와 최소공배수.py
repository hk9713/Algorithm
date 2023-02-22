# 나의 풀이
import math
def solution(n, m):
    return [math.gcd(n,m), (n*m)//math.gcd(n,m)]

# 배운 풀이
def gcdlcm(a, b):
    c,d = max(a,b), min(a,b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [ c, int(a*b/c) ]
    return answer
## 유클리드 호제법
## 2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘 중 하나
## 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘을 말한다.