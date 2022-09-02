from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    q_len = len(queue1) + len(queue2)
    
    while sum1 != sum2:
        if sum1 > sum2:
            curr = queue1.popleft()
            queue2.append(curr)
            sum2 += curr
            sum1 -= curr
        elif sum1 < sum2:
            curr = queue2.popleft()
            queue1.append(curr)
            sum1 += curr
            sum2 -= curr
        answer += 1
    
        if answer > q_len*2:
            answer = -1
            break
        
    return answer