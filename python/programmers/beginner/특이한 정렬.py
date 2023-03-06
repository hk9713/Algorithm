# 나의 풀이
def solution(numlist, n):
    cal_list = list(map(lambda x: x-n, numlist))
    dic = { num:minus for num, minus in zip(numlist, cal_list) }
    answer = sorted(dic.items(), key=lambda x:abs(x[1]))
    result = []
    for i,item in enumerate(answer):
        if i != 0:
            if abs(item[1]) == abs(answer[i-1][1]):
                result.pop()
                result.append(max(item[0],answer[i-1][0]))
                result.append(min(item[0],answer[i-1][0]))
            else:
                result.append(item[0])
        else:
            result.append(item[0])       
    return  result

# 배운 풀이
def solution(numlist, n):
    return sorted(numlist,key = lambda x: [abs(x-n),-x])

# 적용
def solution(numlist, n):
    cal_list = list(map(lambda x: x-n, numlist))
    dic = { num:minus for num, minus in zip(numlist, cal_list) }
    answer = sorted(dic.items(), key=lambda x:(abs(x[1]),-x[1])) 
    return  [i[0] for i in answer]