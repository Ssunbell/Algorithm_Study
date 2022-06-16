from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n = int(input())
standard = list(map(int, input().split()))
standard = deque(standard)
reversed_s = []
for s in standard:
    if s == 1:
        r = 3
    elif s == 2:
        r = 4
    elif s == 3:
        r = 1
    elif s == 4:
        r = 2
    reversed_s.append(r)

reversed_s.reverse()
reversed_s = deque(reversed_s)
candidate = []
while n:
    standard.rotate(1)
    reversed_s.rotate(1)
    n -= 1
    candidate.append(list(standard))
    candidate.append(list(reversed_s))

answer = []
m = int(input())
for _ in range(m):
    s = list(map(int, input().split()))
    if s in candidate:
        answer.append(s)
print(len(answer))
for a in answer:
    print(*a)
