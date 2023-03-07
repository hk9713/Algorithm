# 나의 풀이
def solution(score):
    score = list(map(lambda x:(x[0]+x[1])/2, score))
    rank = sorted(score, reverse=True)
    answer = {}
    for i, num in enumerate(rank, start=1):
        if num in answer:
            continue
        answer[num] = i
    return [answer[s] for s in score]

# 배운 풀이
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]