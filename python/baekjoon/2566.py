# 2566 - 최댓값
# 9x9 격자판에 81개의 자연수 또는 0이 주어진다.
# 출력 - 첫 줄은 최댓값, 둘째 줄은 최댓값이 위치한 행 번호와 열 번호
# 단, 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치만 출력한다.

num_list = []
for _ in range(9):
    input_list = list(map(int, input().split()))
    num_list.append(input_list)

answer = [0,1,1]
for idx, row in enumerate(num_list):
    if max(row) > answer[0]:
        answer[0] = max(row)
        answer[1] = idx+1
        answer[2] = list(row).index(max(row))+1

print(answer[0])
print(answer[1], answer[2])
