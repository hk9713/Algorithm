# 14215 - 세 막대
# 첫 줄에 a, b, c (1<=a,b,c<=100)가 주어진다.
# 세 막대를 이용해서 넓이가 양수인 삼각형을 만들 수 있어야 한다.
# 각 막대의 길이는 마음대로 줄일 수 있다.
# 출력 - 만들 수 있는 삼각형의 가장 큰 둘레

def cal_perimeter(a, b, c):
    max_length = max(a, b, c)
    standard_length = sum([a,b,c]) - max_length

    if standard_length > max_length:
        perimeter = sum([a,b,c])
    else:
        perimeter = standard_length+(standard_length-1)
    
    return perimeter

a, b, c = map(int, input().split())
print(cal_perimeter(a,b,c))
