# 10813 - 공 바꾸기
# N개 바구니, M번 공을 바꾸는 시도
# 처음 바구니에는 바구니 번호와 같은 공이 1개씩 들어있다.
# M번에 걸쳐 i번 바구니와 j번 바구니의 공을 서로 교환한다.
# 출력 - 1번부터 N번까지 바구니에 들어있는 공의 번호(공백으로 구분)

N,M = map(int, input().split())
bucket = [i+1 for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    temp = bucket[i-1]
    bucket[i-1] = bucket[j-1]
    bucket[j-1] = temp
print(*bucket)
