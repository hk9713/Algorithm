# 나의 풀이
n = int(input())
for i in range(1,n+1):
    print("*"*i)

# 배운 풀이
print('\n'.join('*' * (i + 1) for i in range(int(input()))))