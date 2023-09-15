# 1157 - 단어 공부
# 알파벳 대소문자로 이루어진 단어가 주어진다.
# 출력 - 주어진 단어에서 가장 많이 사용된 알파벳(대문자)
# 단, 여러 개가 존재하는 경우에는 ? 를 출력한다.

word = input().upper()
char_dic = {}
for char in word:
    if char in char_dic:
        char_dic[char] += 1
    else:
        char_dic[char] = 1
max_alphabet = [ k for k,v in char_dic.items() if max(char_dic.values())==v]
print( max_alphabet[0] if len(max_alphabet)==1 else "?")
