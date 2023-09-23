# 11005 - 진법 변환 2
# 10진수 N이 주어진다.
# 출력 - 10진법 수 N을 B진법으로 바꾼다.

N, B = map(int, input().split())

num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ""

while N != 0:
    answer += str(num[N%B])
    N = N // B

print(answer[::-1])
