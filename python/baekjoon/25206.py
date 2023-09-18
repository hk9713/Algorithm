# 25206 - 너의 평점은
# 전공평점은 전공과목별 (학점 x 과목평점)의 합을 학점의 총합으로 나눈 값이다.
# 등급이 P인 과목은 계산에서 제외해야 한다.
# 출력 - 20개 과목을 수강한 치훈이의 전공평점

grade_dic = { 'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0 }
total_score = 0
cal_score = 0

for enter in range(20):
    subject, score, grade = map(str, input().split())
    if grade == 'P':
        continue
    total_score += float(score)
    cal_score += float(score)*grade_dic[grade]

print(cal_score/total_score)
