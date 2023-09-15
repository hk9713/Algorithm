# 2908 - 상수
# 서로 같지 않은 두 수 A, B가 주어진다.
# 출력 - 각 수를 반대로 읽었을 때, 더 큰 수

A, B = map(str, input().split())
A = int("".join(reversed(A)))
B = int("".join(reversed(B)))
print(max(A,B))
