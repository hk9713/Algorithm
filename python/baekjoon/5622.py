# 5622 - 다이얼
# 다이얼 전화기에는 2부터 9까지 숫자 아래에 3~4개의 대문자 알파벳이 있다.
# 숫자 하나를 누르면 다이얼이 처음 위치로 돌아간다.
# 숫자 1을 누르려면 2초가 필요하고, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
# 출력 - 대문자로 이루어진 알파벳이 주어졌을 때, 모든 숫자를 누르기 위한 최소 시간

from string import ascii_uppercase

alphabet_list = [*ascii_uppercase]
num = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
dial_dic = dict(zip(alphabet_list, num))

word = input()
time = len(word)
for i in word:
    time += dial_dic[i]
print(time)
