# 5086 - 배수와 약수
# 두 수가 주어졌을 때, 다음 3가지 관계로 구분된다.
# (1) 첫 번째 숫자가 두 번째 숫자의 약수이다.
# (2) 첫 번째 숫자가 두 번째 숫자의 배수이다.
# (3) 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.
# 출력 - (1)이면 factor, (2)면 multiple, (3)이면 neither

def solution() :
    num1, num2 = map(int, input().split()) 

    if num1 == 0 and num2 == 0:
        None
    else:
        if num2 % num1 == 0 :
            print("factor")
        elif num1 % num2 == 0 :
            print("multiple")
        else:
            print("neither")
        solution()

solution()
