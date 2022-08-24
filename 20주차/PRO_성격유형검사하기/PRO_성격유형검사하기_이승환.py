def solution(survey, choices):
    answer = ''
    points = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for i in range(len(survey)):
        if choices[i] == 1:
            points[survey[i][0]] += 3
        elif choices[i] == 2:
            points[survey[i][0]] += 2
        elif choices[i] == 3:
            points[survey[i][0]] += 1
        elif choices[i] == 5:
            points[survey[i][1]] += 1
        elif choices[i] == 6:
            points[survey[i][1]] += 2
        elif choices[i] == 7:
            points[survey[i][1]] += 3
            
    if points["T"] > points["R"]:
        answer += "T"
    elif points["T"] == points["R"]:
        answer += "R"
    else:
        answer += "R"
    if points["C"] > points["F"]:
        answer += "C"
    elif points["C"] == points["F"]:
        answer += "C"
    else:
        answer += "F"
    if points["J"] > points["M"]:
        answer += "J"
    elif points["J"] == points["M"]:
        answer += "J"
    else:
        answer += "M"
    if points["A"] > points["N"]:
        answer += "A"
    elif points["A"] == points["N"]:
        answer += "A"
    else:
        answer += "N"
        
    return answer