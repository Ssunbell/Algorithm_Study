from collections import deque

tmp = deque()
case = []
score = []
    
def makeCase(n, cnt):
    if cnt == 11:
        if sum(tmp) == n:
            case.append(tuple(tmp))
        return
    
    for i in range(0, n+1):
        if sum(tmp) > n:
            continue
        tmp.append(i)
        makeCase(n, cnt+1)
        tmp.pop()
            
def solution(n, info):
    makeCase(n, 0)
    for c in case:
        tmp = 0
        for i in range(11):
            if c[i] == 0 and info[i] == 0:
                pass
            elif c[i] > info[i]:
                tmp += (10 - i) # 라이언 승
            elif c[i] <= info[i]:
                tmp -= (10 - i) # 어피치 승
        score.append(tmp)
        
    if max(score) < 1:
        return [-1]
        
    max_count = score.count(max(score))
    if  max_count > 1:
        max_list = []
        while max_count:
            tmp_idx = score.index(max(score))
            score.pop(tmp_idx)
            max_list.append(list(case.pop(tmp_idx)))
            max_count -= 1
        answer = sorted(max_list, key= lambda x : (-x[10], -x[9], -x[8], -x[7], -x[6],
                                            -x[5], -x[4], -x[3], -x[2], -x[1], -x[0]))[0]
    else:
        answer = list(case[score.index(max(score))])
    
    return answer

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
print(solution(n, info))