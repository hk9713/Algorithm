# 나의 풀이
def solution(dots):
    x = []
    y = []
    for i in dots:
        x.append(i[0])
        y.append(i[1])
    return (max(x)-min(x))*(max(y)-min(y))

# 배운 풀이
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])