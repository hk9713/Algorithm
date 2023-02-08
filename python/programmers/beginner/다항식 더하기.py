# 나의 풀이
def solution(polynomial):
    x_list = []
    num_list = []
    num = polynomial.split(' + ')
    for n in num:
        if n[-1] == "x":
            if n[:-1] == "":
                x_list.append(1)
            else:
                x_list.append(int(n[:-1]))
        else:
            num_list.append(int(n))
    cal_x = sum(x_list)
    cal_n = sum(num_list)

    if cal_x == 1:
        return "x + "+str(cal_n) if cal_n > 0 else "x"
    elif cal_n == 0:
        return str(cal_x)+"x"
    elif cal_x == 0:
        return str(cal_n)
    else:
        return str(cal_x)+"x + "+str(cal_n)

# 배운 풀이
def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'