# 나의 풀이
def solution(slice, n):
    return (n-1) // slice + 1

# 배운 풀이
def solution(slice, n):
    d, m = divmod(n, slice)
    return d + int(m!=0)