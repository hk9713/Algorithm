# 나의 풀이
def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        for i in range(1,len(word)+1):
            if i % 2 != 0 :
                answer += word[i-1].upper()
            else:
                answer += word[i-1].lower()
        answer += ' '
    return answer[:-1]

# 배운 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))