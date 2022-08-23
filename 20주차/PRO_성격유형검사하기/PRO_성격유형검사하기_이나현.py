def solution(survey, choices):
    l = len(survey)
    point = [0,3,2,1,0,1,2,3]
    reverse = set(['TR', 'FC', 'MJ', 'NA'])
    score = [[0, 0] for _ in range(4)] #각각 [['R', 'T'], ['C', 'F'], [...], [...]]의 합산 점수이다.
    name = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    answer = ''
    for i in range(l):
        if survey[i] == 'RT' or survey[i] == 'TR':
            index = 0 # 지표 인덱스
        elif survey[i] == 'CF' or survey[i] == 'FC':
            index = 1
        elif survey[i] == 'JM' or survey[i] == 'MJ':
            index = 2
        else: #AN
            index = 3
        choice = choices[i]
        if choice < 4:
            if survey[i] not in reverse: #알파벳 반대 순서의 servey[i]가 아니라면, ex)'FC' -> 반대
                score[index][0] += point[choice]
            else:
                score[index][1] += point[choice]
        else:
            if survey[i] not in reverse:
                score[index][1] += point[choice]
            else:
                score[index][0] += point[choice]
    
    for index in range(4):
        if score[index][0] >= score[index][1]:
            answer += name[index][0]
        else:
            answer += name[index][1]
    return answer