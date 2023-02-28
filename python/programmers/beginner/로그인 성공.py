# 나의 풀이
def solution(id_pw, db):
    if id_pw in db:
        return "login"
    elif any(id_pw[0] in data for data in db):
        return "wrong pw"
    else:
        return "fail"

# 배운 풀이
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"
## 바다코끼리 연산자 :=
## 변수 := 표현식 ; 표현식의 결과를 변수에 할당하고, 동시에 반환한다.
## python 3.8부터 사용 가능