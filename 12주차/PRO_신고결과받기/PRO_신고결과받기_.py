def solution(id_list, report, k):
    report = list(set(report))
    dict_report = {id : [] for id in id_list}
    dict_reported = {id : 0 for id in id_list}
    for r in report:
        re_id, re = r.split(' ')
        dict_report[re_id].append(re)
        dict_reported[re] += 1

    list_stop = []
    for re, c in dict_reported.items():
        if c >= k:
            list_stop.append(re)
    
    answer = [0] * len(id_list)
    for i, list_re in enumerate(dict_report.values()):
        for stop in list_stop:
            if stop in list_re:
                answer[i] += 1

    return answer

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list, report, k))