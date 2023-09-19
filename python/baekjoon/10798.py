# 10798 - 세로 읽기
# 다섯줄의 글자들(최소 1개, 최대 15개)이 주어진다.
# 출력 - 주어진 글자들을 빈칸없이 세로로 읽는다.

word_list = []
for _ in range(5):
    word_list.append( list(map(str, input())))

answer = ""
for i in range(15):
    for j in range(5):
        if i < len(word_list[j]):
            answer += word_list[j][i]

print(answer)
