def solution(info, query):
    answer = []
    resume = []
    for s in info:
        lan, job, career, soulfood, score = s.split()
        resume.append([lan,job,career,soulfood,score])
    
    for q in query:
        lan, job, career, etc = q.split(" and ")
        soulfood, score = etc.split()
        candidate = 0
        for r in resume:
            if r[0] != lan and lan != "-":
                continue
            if r[1] != job and job != "-":
                continue
            if r[2] != career and career != "-":
                continue
            if r[3] != soulfood and soulfood != "-":
                continue
            if int(r[4]) < int(score):
                continue
            candidate += 1
        answer.append(candidate)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))