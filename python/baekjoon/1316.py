# 1316 - 그룹 단어 체커
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# N = 입력 받을 단어 개수
# 출력 - N개의 단어 중 그룹 단어의 개수 

N = int(input())
not_group_word = []

for _ in range(N):
    word = input()
    temp = []
    for char in word:
        if char not in temp:
            temp.append(char)
        elif char == temp[-1]:
            continue
        else:
            not_group_word.append(word)
            break

print(N-len(not_group_word))
