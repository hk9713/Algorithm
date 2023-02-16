# 나의 풀이
def solution(board):
    answer = 0
    limit = len(board)
    new = [[0 for i in range(limit)] for j in range(limit)]
    for i in range(limit):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                new[i][j] = 1
                if i > 0:
                    if j > 0:
                        new[i - 1][j - 1], new[i - 1][j], new[i][j - 1] = 1, 1, 1
                    if j < limit - 1:
                        new[i - 1][j + 1], new[i - 1][j], new[i][j + 1] = 1, 1, 1
                if i < limit - 1:
                    if j > 0:
                        new[i + 1][j - 1], new[i + 1][j], new[i][j - 1] = 1, 1, 1
                    if j < limit - 1:
                        new[i + 1][j + 1], new[i + 1][j], new[i][j + 1] = 1, 1, 1
    for i in range(len(new)):
        for j in range(len(new[i])):
            if new[i][j] == 0:
                answer += 1
    return answer

# 배운 풀이
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)
