def solution(survey, choices):
    cha_dict = {'first':{'R': 0, 'T': 0},
                'second':{'C':0, 'F':0},
                'third':{'J':0, 'M': 0},
                'forth':{'A':0, 'N':0}}
    
    for s, c in zip(survey, choices):
        score = c - 4

        if score <= 0:
            key = s[0]
            value = (-1) * score
            
        elif score > 0:
            key = s[1]
            value = score
        
        if 'R' in s:
            cha_dict['first'][key] += value
        elif 'C' in s:
            cha_dict['second'][key] += value
        elif 'J' in s:
            cha_dict['third'][key] += value
        elif 'A' in s:
            cha_dict['forth'][key] += value
            
    answer = ''
    for row in [['first','R','T'], ['second','C', 'F'],['third','J','M'], ['forth','A','N']]:
        if cha_dict[row[0]][row[1]] >= cha_dict[row[0]][row[2]]:
            answer += row[1]
        else:
            answer += row[2]
            
    return answer