from collections import deque
def solution(queue1, queue2): 
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total_len = len(queue1)+len(queue2)
    answer = 0
    while sum1 != sum2:
        if sum1 > sum2:
            x = queue1.popleft()
            sum1 -= x
            sum2 += x
            queue2.append(x)
        else: # sum2 > sum1
            x = queue2.popleft()
            sum2 -= x
            sum1 += x
            queue1.append(x)
        answer += 1
        if answer > total_len+2:
            return -1
    return answer
