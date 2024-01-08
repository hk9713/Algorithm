# 15894 - 수학은 체육과목 입니다
# 첫 번째 줄에 가장 아랫부분의 정사각형 개수 n이 주어진다. (1 ≤ n ≤ 109)
# 정사각형 한 변의 길이는 1이다.
# 출력 - 해당 도형의 둘레 길이

def cal_length(N):
    length = N*3 + N
    return length

n = int(input())
print( cal_length(n) )
