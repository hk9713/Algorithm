# 나의 풀이
from collections import Counter

def solution(array):
    count = Counter(array).most_common()
    if len(count) == 1 or count[0][1]!=count[1][1]:
        return count[0][0]
    else:
        return -1

# 배운 풀이
def solution(array):
    while len(array)!=0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i==0:
            return a
    return -1