# 2581 - 소수
# 자연주 M과 N이 주어진다.
# 출력 - 첫째 줄은 M 이상 N 이하의 자연수 중 소수들의 합, 둘째 줄은 그 중 최솟값
# 단, M 이상 N 이하의 자연수 중 소수가 없을 경우는 첫쨰 줄에 -1을 출력한다.

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

M = int(input())
N = int(input())

num_list = [ num for num in range(M, N+1) ]
TF_list = list(map(is_prime, num_list))

answer  = [ i+M for i, x in enumerate(TF_list) if x == True ]

if len(answer) == 0 :
    print(-1)
else:
    print(sum(answer), min(answer), sep='\n')
