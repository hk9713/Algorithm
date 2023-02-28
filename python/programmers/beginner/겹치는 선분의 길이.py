# 나의 풀이
def solution(lines):
    a,b,c = sorted(lines, key=lambda x:x[0])
    answer = []
    if a[1] > b[0]:
        limit = min(a[1],b[1])
        answer.append([b[0],limit])
    if a[1] > c[0]:
        limit = min(a[1],c[1])
        answer.append([c[0],limit])
    if b[1] > c[0]:
        limit = min(b[1],c[1])
        answer.append([c[0],limit])
    
    if len(answer)==0:
        return 0
    elif len(answer)==1:
        return answer[0][1]-answer[0][0]
    elif len(answer)==2:
        if answer[0][1]>=answer[1][0]:
            return answer[1][1]-answer[0][0]
        else:
            return (answer[0][1]-answer[0][0])+(answer[1][1]-answer[1][0])
    else:
        a,b,c = answer
        d = [a[0],max(a[1],b[1])]
        if d[1]>=c[0]:
            d = [min(d[0],c[0]),max(d[1],c[1])]
            return d[1]-d[0]
        else:
            return (d[1]-d[0]) + (c[1]-c[0])      

# 배운 풀이
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
## &는 집합의 교집합을, |는 집합의 합집합을 추출한다.