# 10810 - 공 넣기
# N개 바구니, M번 공을 넣는 시도
# 공을 넣는 방법 ( i, j, k ) - i번 바구니에서 j번 바구니까지에 k번 번호가 적힌 공을 넣는다
# 바구니에는 같은 번호의 공만 들어갈 수 있으며, 이미 공이 있는 경우 새로운 공을 넣는다.
# 출력 - 1번 바구니부터 N번 바구니에 들어있는 공의 번호 (공백으로 구분)

N, M = map(int, input().split())
bucket = [0]*N
for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i, j+1):
        if bucket[idx-1] != k:
            bucket[idx-1] = k
        else:
            continue
print(*bucket)
