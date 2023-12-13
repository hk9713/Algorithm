# 11653 - 소인수분해
# 정수 N( 1 <= N <= 10000000 )가 주어진다.
# 출력 - N의 소인수분해 결과(한 줄에 하나씩 오름차순으로)

def solution(N):
    num = 2

    while num <= N:
        if N % num == 0:
            print(num)
            N = N/num
        else:
            num += 1

N = int(input())
solution(N)
