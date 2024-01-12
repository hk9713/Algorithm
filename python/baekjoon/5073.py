# 5073 - 삼각형과 세 변
# 각 줄에는 1000을 넘지 않는 양의 정수 3개가 입력된다.
# 마지막 줄은 0 0 0 이며, 이 줄은 계산하지 않는다.
# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우
# Invalid : 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않은 경우
# 출력 - Equilateral, Isosceles, Scalene, Invalid 중 하나

def decision_triange(a, b, c):
    max_num = max([a,b,c])

    if max_num >= sum([a,b,c])-max_num:
        answer = "Invalid"
    elif a==b and b==c and c==a:
        answer = "Equilateral"
    elif a!=b and b!=c and c!=a:
        answer = "Scalene"
    else:
        answer = "Isosceles"

    return answer

while True:
    a,b,c = map(int, input().split())
    if a==b and b==c and c==0:
        break
    else:
        print(decision_triange(a,b,c))
