# 나의 풀이
def solution(s):
    check = [char for char in s.upper()]
    if check.count("P") == check.count("Y"):
        return True
    else: 
        return False

# 배운 풀이
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')