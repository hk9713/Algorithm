# 나의 풀이
def solution(s):
    length = len(s)
    return s[length//2] if length % 2 != 0 else s[length//2-1:length//2+1]

# 배운 풀이
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]