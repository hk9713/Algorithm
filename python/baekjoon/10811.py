# 10811 - 바구니 뒤집기
# N개의 바구니, M번 뒤집기 시도
# M번, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만든다.
# 출력 - 가장 왼쪽 바구니부터 적혀있는 번호 (공백으로 구분)


N, M = map(int, input().split())
bucket = [i+1 for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    bucket[i-1:j] = bucket[i-1:j][::-1]
print(*bucket)
