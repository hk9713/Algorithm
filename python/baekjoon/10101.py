# 10101 - 삼각형 외우기
# 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. (단, 각은 0보다 크고 180보다 작다)
# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
# 출력 - Equilateral, Isosceles, Scalene, Error 중 하나

def judgment_triangle(a, b, c):

    if a+b+c!=180 :
        answer = "Error"
    elif a==b and b==c :
        answer = "Equilateral"
    elif a==b or b==c or a==c:
        answer = "Isosceles"
    else:
        answer = "Scalene"
    
    return answer

a,b,c = map(int, [input() for _ in range(3)])
print( judgment_triangle(a,b,c) )
