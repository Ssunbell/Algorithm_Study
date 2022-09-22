def lower_binary_search(arr:list, score:int) -> int:
    start = 0
    end = len(arr)
    
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= score:
            end = mid
        else:
            start = mid + 1
    return start

def make_case() -> dict:
    case = {}
    for c1 in ['cpp', 'java', 'python', '-']:
        for c2 in ['backend', 'frontend', '-']:
            for c3 in ['junior', 'senior','-']:
                for c4 in ['chicken', 'pizza', '-']:
                    case[c1+c2+c3+c4] = []
    return case
            

def solution(info, query):
    case_dict = make_case()
    for i in info:
        lan, cat, car, food, score = i.split()
        for i in [lan, '-']:
            for j in [cat, '-']:
                for k in [car, '-']:
                    for z in [food, '-']:
                        case_dict[i+j+k+z].append(int(score))
    
    for key in case_dict:
        case_dict[key].sort()
    
    answer = []
    for where in query:
        language, category, career, where2 = where.split(' and ')
        food, score = where2.split()
        
        score_arr = case_dict[language + category + career + food]
        idx = lower_binary_search(score_arr, int(score))

        answer.append(len(score_arr) - idx)
    
    return answer

## 정확도 통과 but 효율성 x
# def solution(info, query):
#     info_query = []
#     select = ['language', 'category', 'career', 'food', 'score']
    
#     for i in info:
#         [lan, cat, car, foo, sco] = i.split()
#         info_query.append(
#             {'language': lan, 'category': cat,
#             'career': car, 'food': foo, 'score': int(sco)}
#         )

#     answer = []
#     for where in query:
#         cnt = 0
#         where = ' '.join(where.split(' and ')).split(' ')
#         where_set = set(where)
#         standard_score = int(where.pop())
#         info_query_from = [info for info in info_query
#                            if info['score'] >= standard_score]
        
#         if '-' in where_set and len(where_set) == 2:
#             cnt = len(info_query_from)
                    
#         else:
#             for iqf in info_query_from:
#                 check = True
#                 for idx, cond in enumerate(where):
#                     if cond == '-':
#                         continue
#                     elif iqf[select[idx]] != cond:
#                         check = False
#                         break
#                 if check:
#                     cnt+=1
                        
#         answer.append(cnt)
    
#     return answer