# 9506 - 약수들의 합
# 테스트 케이스마다 한 줄 간격으로 n이 주어진다.
# 입력의 마지막엔 -1이 주어진다.
# 출력 - n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타낸다.
# n이 완전수가 아니라면, n is NOT perfect. 를 출력한다.

def solution():
    n = int(input())

    if n == -1 :
        None
    else:
        num_list = [i+1 for i in range(n) if (n % (i+1) == 0 and n!= i+1)]
        if sum(num_list) == n:
            print(f"{n} =",end=' ')
            print(*num_list, sep=' + ')
        else:
            print(f"{n} is NOT perfect.")
        solution()

solution()
