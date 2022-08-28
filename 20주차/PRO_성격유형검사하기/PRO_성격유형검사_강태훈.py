MBTI = [["R", "T"],["C", "F"],["J", "M"],["A", "N"]]
test_case = ["RT","TR","CF","FC","JM","MJ","AN","NA"]
test_idx = {tc: i//2 for i, tc in enumerate(test_case)}
response_value = {i:(i//4, abs(i-4)) for i in range(1, 8)}

def solution(survey, choices):
    answer = ''
    user_response = [{i:0 for i in case}for case in MBTI]
    
    for test, choice in zip(survey, choices):
        name, value = response_value[choice]
        user_response[test_idx[test]][test[name]] += value
        
    for i in range(4):
        user_response[i] = sorted(user_response[i].items(), key = lambda x: (-x[1], x[0]))
        answer += user_response[i][0][0]

    return answer

tc = [[["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]],[["TR", "RT", "TR"], [7, 1, 3]]]
for a, b in tc:
    print(solution(a, b))