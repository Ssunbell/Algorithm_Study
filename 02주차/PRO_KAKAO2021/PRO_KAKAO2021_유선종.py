def solution(const):
    dic = {
        '0' : 'zero',
        '1' : 'one',
        '2' : 'two',
        '3' : 'three',
        '4' : 'four',
        '5' : 'five',
        '6' : 'six',
        '7' : 'seven',
        '8' : 'eight',
        '9' : 'nine'
    }
    
    total = ''
    alp = ''
    dic_key = list(dic.keys())
    dic_value = list(dic.values())
    
    for i in list(const):
        if i not in dic_key:
            alp += i
            if alp in dic_value:
                total += dic_key[dic_value.index(alp)]
                alp = ''
        else:
            total += i
    return total

print(solution("one4seveneight"))

####################################

def solution(s):

    letter = {'zero': '0','one': '1', 'two': '2', 'three': '3', 'four': '4', 
              'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for key, value in letter.items():
        if key in s:
            s = s.replace(key, value)
            
    return int(s)