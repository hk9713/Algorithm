# 2675 - 문자열 반복
# 테스트 케이스 개수 T
# T만큼 반복하며, 반복횟수 R과 문자열 S가 공백으로 구분되어 주어진다.
# 출력 - S의 각 문자를 R번 반복한 새 문자열 P

T = int(input())
for _ in range(T):
    R, S = map(str, input().split())
    P = ""
    for char in S:
        P += char*int(R)
    print(P)
