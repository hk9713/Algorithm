# 2941 - 크로아티아 알파벳
# 크로아티아 알파벳은 다음과 같이 변경해서 사용한다. 
# [ 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]
# 위 목록에 없는 알파벳은 한 글자씩 센다.
# 출력 - 주어진 단어의 크로아티아 알파벳 개수

word = input()
alphabet_list = [ 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]
for char in alphabet_list:
    word = word.replace(char, "x")
print(len(word))
