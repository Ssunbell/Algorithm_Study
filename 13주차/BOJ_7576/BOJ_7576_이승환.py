import sys
from collections import deque

input_s = lambda : sys.stdin.readline().strip()

m,n = map(int,input_s().split())
box = []
for _ in range(n):
    box.append(list(map(int,input_s().split())))

q = deque()
depth_chart = dict()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i,j))
            depth_chart[(i,j)] = 0

di = [1,0,-1,0]
dj = [0,1,0,-1]

while q:
    curr = q.popleft()

    for i in range(4):
        next = (curr[0]+di[i],curr[1]+dj[i])
        if next[0] < 0 or next[1] < 0 or next[0] >= n or next[1] >= m:
            continue
        if box[next[0]][next[1]] == -1:
            continue
        if box[next[0]][next[1]] == 0:
            box[next[0]][next[1]] = 1
            q.append(next)
            depth_chart[next] = depth_chart[curr] + 1
check = False
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            check = True
            break
if check:
    result = -1
else:
    result = max(depth_chart.values())

print(result)
    