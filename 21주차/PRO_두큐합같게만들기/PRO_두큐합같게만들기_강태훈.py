from collections import deque
def solution(queue1, queue2):
    s1, s2, l1, l2, answer = sum(queue1), sum(queue2), len(queue1), len(queue2), 0
    if (s1 + s2) % 2 == 1:
        return -1
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while s1 != s2:
        if answer > (l1 + l2) * 2:
            return -1
        if s1 < s2:
            answer += 1
            temp = queue2.popleft()
            s2 -= temp
            s1 += temp
            queue1.append(temp)
        elif s1 > s2:
            answer += 1
            temp = queue1.popleft()
            s1 -= temp
            s2 += temp
            queue2.append(temp)
    return answer