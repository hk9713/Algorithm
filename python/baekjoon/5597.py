# 5597 - 과제 안 내신 분
# 30명의 학생 중 과제를 제출 안 한 2명의 출석번호를 구한다.
# 출력 - 오름차순, 2줄

student = [i+1 for i in range(30)]
for _ in range(28):
    submit = int(input())
    student.remove(submit)
print(*student, sep='\n')
