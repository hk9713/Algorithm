# 나의 풀이
def solution(s):
    if len(s)==4 or len(s)==6:
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False

# 배운 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]