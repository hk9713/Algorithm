# 나의 풀이
def solution(spell, dic):
    spell.sort()
    for d in dic:
        if len(d) == len(spell):
            temp = [char for char in d]
            temp.sort()
            if temp == spell:
                return 1
    return 2

# 배운 풀이
def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2