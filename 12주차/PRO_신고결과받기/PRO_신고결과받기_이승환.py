# 틀린거
def solution(id_list, report, k):
    answer = []
    
    id_rep = {i : [] for i in id_list}
    id_reported = {i : [] for i in id_list}

    for rep in report:
        rep_by, rep_person = rep.split()
        id_rep[rep_by].append(rep_person)
        id_reported[rep_person].append(rep_by)
    
    reported_list = []
    for i in id_list:
        report_set = set(id_reported[i])
        if len(report_set) >= k:
            reported_list.append(i)
    
    for i in id_list:
        mail = 0
        for rep_person in id_rep[i]:
            if rep_person in reported_list:
                mail += 1
        answer.append(mail)
        
    return answer

# 맞은거
def solution(id_list, report, k):
    answer = []
    
    report = set(report)
    
    id_rep = {i : [] for i in id_list}
    id_reported = {i : [] for i in id_list}
    
    for rep in report:
        rep_by, reported = rep.split()
        id_rep[rep_by].append(reported)
        id_reported[reported].append(rep_by)
    
    reported_person = []
    for i in id_list:
        if len(id_reported[i]) >= k:
            reported_person.append(i)
            
    for i in id_list:
        mail = 0
        for rep_person in id_rep[i]:
            if rep_person in reported_person:
                mail += 1
        answer.append(mail)
        
    return answer