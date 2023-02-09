# 나의 풀이
def solution(sides):
    limit = sum(sides)
    max_s, min_s = max(sides), min(sides)
    answer = []
    for i in range(max_s-min_s+1, max_s):
        answer.append(i)
    while max_s < limit:
        answer.append(max_s)
        max_s += 1
    return len(answer)

# 배운 풀이
def solution(sides):
    return 2 * min(sides) - 1
'''
# 삼각형의 두 변을 알고 있을 때

1) 이미 아는 변 중의 하나가 가장 긴 경우 (a<b)
    b < a + c
    b - a < c

2) 모르는 변이 가장 긴 경우
    c < a + b
    
따라서,
b - a < c < a + b
c의 개수는 우측항 - 좌측항 - 1 이므로 
(a + b) - (b - a) -1 
= 2a - 1 
'''