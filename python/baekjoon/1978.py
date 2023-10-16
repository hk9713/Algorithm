# 1978 - 소수 찾기
# 첫 줄에 수의 개수 N이 주어진다.
# 출력 - N개의 수들 중 소수의 개수

import math

N = int(input())
numbers = [0]*N
numbers = list(map(int,input().split()))

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

check_numbers = list(map(is_prime, numbers))
print(check_numbers.count(True))
