# 2745 - 진법 변환
# B진법 수 N이 주어진다.
# 출력 - 10진법으로 바꾼 N

N, B = map(str, input().split())

num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = ''.join(reversed(N))

result = 0
for i in range(len(N)-1, -1, -1):
    temp = num.index(N[i]) * (int(B)**i)
    result += temp

print(result)
