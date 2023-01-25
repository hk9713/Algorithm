# 나의 풀이
def solution(my_string):
    vowel = ['a','e','i','o','u']
    for v in vowel:
        my_string = my_string.replace(v,"")
    return my_string

# 배운 풀이
def solution(my_string):
    return "".join([i for i in my_string if not (i in "aeiou")])