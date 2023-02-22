# 나의 풀이
a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print( "*" * a )

# 배운 풀이
a, b = map(int, input().strip().split(' '))
print( ('*' * a + '\n') * b )