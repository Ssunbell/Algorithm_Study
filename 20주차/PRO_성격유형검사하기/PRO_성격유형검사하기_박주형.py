# 성격유형 점수 동일하면 사전 순으로 빠른 유형

def solution(survey, choices):
    indicators = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }

    answer = ''

    n = len(survey)

    for i in range(n):
        choices[i] = choices[i] - 4
    

    for i in range(n):
        if choices[i] < 0:
            indicators[survey[i][0]] -= choices[i]

        elif choices[i] == 0:
            continue

        else:
            indicators[survey[i][1]] += choices[i]

    
    print(indicators)


    if indicators['R'] >= indicators['T'] :
        answer += 'R'

    if indicators['T'] > indicators['R'] :
        answer += 'T'

    if indicators['C'] >= indicators['F'] :
        answer += 'C'

    if indicators['F'] > indicators['C'] :
        answer += 'F'

    if indicators['J'] >= indicators['M'] :
        answer += 'J'

    if indicators['M'] > indicators['J'] :
        answer += 'M'

    if indicators['A'] >= indicators['N'] :
        answer += 'A'

    if indicators['N'] > indicators['A'] :
        answer += 'N'


    return answer

    
solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])