import sys
from collections import deque

t = int(input())

for _ in range(t):
    input_s = lambda : sys.stdin.readline().strip()
    n, idx = map(int,input_s().split())
    pri = list(map(int,input_s().split()))

    q = deque()

    for i in range(n):
        q.append((pri[i],i))

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
            if curr[1] == idx:
                break
    print(pnum)

