# 10809 - 알파벳 찾기
# 소문자 단어 S
# 출력 - 단어 S에 대해 a부터 z까지 각 알파벳이 등장하는 위치 (없으면 -1)

from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)

S = input()
word_dic = {}
for num, char in enumerate(S):
    if char not in word_dic:
        word_dic[char] = num

for idx, alphabet in enumerate(alphabet_list):
    if alphabet in word_dic:
        alphabet_list[idx] = word_dic[alphabet]
    else:
        alphabet_list[idx] = -1

print(*alphabet_list)
