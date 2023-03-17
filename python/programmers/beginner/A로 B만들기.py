# 나의 풀이
def solution(before, after):
    list_b = sorted(list(before))
    list_a = sorted(list(after))
    return int(list_b == list_a)

# 배운 풀이
def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0