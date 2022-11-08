from collections import deque

def solution(rc, operations):
    r,l = deque(),deque()
    for i in range(len(rc)):
        l.append(rc[i][0])
        r.append(rc[i][-1])
    c = deque(deque(rc[i][1:-1]) for i in range(len(rc)))
    for op in operations:
        if op == 'ShiftRow':
            c.appendleft(c.pop())
            r.appendleft(r.pop())
            l.appendleft(l.pop())
        else:
            c[0].appendleft(l.popleft())
            c[-1].append(r.pop())
            r.appendleft(c[0].pop())
            l.append(c[-1].popleft())
    return [[l[i], *c[i], r[i]] for i in range(len(rc))]

print(solution(	[[1, 2], [2, 3]], ["Rotate"]))