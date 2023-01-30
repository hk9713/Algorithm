# 나의 풀이
import collections
def solution(s):
    count_char = collections.Counter(s)
    return ''.join(sorted([c for c in count_char.keys() if count_char[c]==1]))

# 배운 풀이
def solution(s):
    return ''.join(sorted([ ch for ch in set(s) if s.count(ch) ==1 ]))