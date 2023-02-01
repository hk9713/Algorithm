# 나의 풀이
def solution(quiz):
    question = list(map(lambda x: str(eval(x.split(' = ')[0])), quiz))
    result = list(map(lambda x: x.split(' = ')[1], quiz))
    answer = []
    for i in range(0, len(quiz)):
        if question[i] == result[i]:
            answer.append("O")
        else:
            answer.append("X")
    return answer

# 배운 풀이
def solution(quiz):
    answer = []
    for q in quiz:
        L,R = q.split(' = ')
        a,op,b = L.split()
        if op=='+':
            result = 'O' if int(a)+int(b)==int(R) else 'X'
            answer.append(result)
        else:
            result = 'O' if int(a)-int(b)==int(R) else 'X'
            answer.append(result)
    return answer