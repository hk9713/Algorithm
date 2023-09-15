# 10988 - 팰린드롬인지 확인하기
# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다.
# 출력 - 팰린드롬이면 1, 아니면 0

word = input()
read = "".join(reversed(word))

print(1 if word == read else 0)
