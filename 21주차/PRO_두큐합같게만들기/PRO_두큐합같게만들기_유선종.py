from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    half_sum = (q1_sum + q2_sum) // 2
    limit = (len(queue1) + len(queue2)) * 2
    cnt = 0

    while queue2:
        if cnt == limit:
            break
        if q1_sum == half_sum:
            return cnt
        elif q1_sum > half_sum:
            q1_sum -= queue1.popleft()
        else:
            queue1.append(queue2.popleft())
            q1_sum += queue1[-1]
        cnt += 1
        
    return -1