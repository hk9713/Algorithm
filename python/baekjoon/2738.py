# 2738 - 행렬 덧셈
# 행렬의 크기 N과 M이 주어진다.
# 출력 - N*M크기의 두 행렬 A와 B를 더한 행렬

N, M = map(int, input().split())

A = []
B = []

for num in range(1, 2*N+1):
    entered_num = list(map(int,input().split()))
    if num <= N:
        A.append(entered_num)
    else:
        B.append(entered_num)

for i in range(N):
    answer = []
    for j in range(M):
        answer.append(A[i][j]+B[i][j])
    print(*answer)
