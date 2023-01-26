# 나의 풀이
def solution(s):
    words = s.split()
    while "Z" in words:
        i = words.index("Z")
        del words[i]
        del words[i-1]
    return sum(map(int, words))