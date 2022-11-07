from collections import deque


def solution(rc, operations):
    mid = deque([deque(i[1:-1]) for i in rc])
    left = deque([i[0] for i in rc])
    right = deque(i[-1] for i in rc)
    for op in operations:
        if op == 'ShiftRow':
            mid.appendleft(mid.pop())
            left.appendleft(left.pop())
            right.appendleft(right.pop())
        if op == 'Rotate':
            mid[0].appendleft(left.popleft())
            right.appendleft(mid[0].pop())
            mid[-1].append(right.pop())
            left.append(mid[-1].popleft())
    return [[i]+list(j)+[k] for i, j, k in zip(left, mid, right)]
