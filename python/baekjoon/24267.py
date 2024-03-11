# 24267 - 알고리즘의 수행 시간 6
# 첫 줄에 입력의 크기 n (1<=n<=500000)이 주어진다.
# MenOfPassion 알고리즘 수행 시간을 출력한다.
# 출력 - 첫 줄에는 코드1의 수행 횟수
# 출력 - 둘째 줄에는 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수
# 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''

n = int(input())
cnt = 0
for i in range(n-2):
    cnt += (n-(i+1))*(n-(i+2))//2
print(cnt)
print(3)
