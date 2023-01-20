# 나의 풀이
morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }

def solution(letter, morse):
    return ''.join(morse[i] for i in letter.split(" "))

# 배운 풀이
def solution(letter, morse):
    return ''.join(map(lambda w: morse[w], letter.split( )))