# 2501 - 약수 구하기
# 두 개의 자연수 N과 K가 주어진다.
# 출력 - N의 약수들 중 K번째로 작은 수
# 단, N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력한다.

N, K = map(int, input().split()) 
num_list = [ i+1 for i in range(N) if N % (i+1) == 0 ]

if len(num_list) < K:
    print(0)
else:
    print(num_list[K-1])
