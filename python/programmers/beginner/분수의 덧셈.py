# 나의 풀이
import math

def lcm(a,b):
    return (a * b) // math.gcd(a,b) 

def solution(numer1, denom1, numer2, denom2):
    l = lcm(denom1, denom2)
    f = [numer1*(l//denom1)+numer2*(l//denom2), l]
    g = math.gcd(f[0],f[1])
    f = [f[0]//g if (f[0]%g==0) else f[0], f[1]//g if (f[1]%g==0) else f[1]]
    return f

# 배운 풀이
def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]