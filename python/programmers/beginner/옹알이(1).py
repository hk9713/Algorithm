# 나의 풀이
def solution(babbling):
    able_list = ["aya", "ye", "woo", "ma"]
    answer = 0
    for word in babbling:
        for able in able_list:
            word = word.replace(able,',')
        if len(word.replace(',','')) == 0:
            answer +=1        
    return answer

# 배운 풀이
def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            b = b.replace(w, ' ', 1)
        if len(b.strip()) == 0:
            c += 1
    return c