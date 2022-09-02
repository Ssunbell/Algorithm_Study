from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i],i))
        
    check = False
    pnum = 0
    while q:
        curr = q.popleft()
        for j in range(len(q)):
            if q[j][0] > curr[0]:
                q.append(curr)
                check = True
                break
            else:
                check = False
        if check == False:
            pnum += 1
            if curr[1] == location:
                break
    answer = pnum
    return answer