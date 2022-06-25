import sys
from collections import deque

input_s = lambda : sys.stdin.readline().strip()

n,m = map(int,input_s().split())

maze = [list(input_s()) for _ in range(n)]

dest = (n-1,m-1)
q = deque()
q.append((0,0))
visited = deque()
dn = [0,1,0,-1]
dm = [1,0,-1,0]
depth_chart = dict()
depth_chart[(0,0)] = 1

while q:
    curr = q.popleft()
    visited.append(curr)

    for i in range(4):
        next = (curr[0]+dn[i],curr[1]+dm[i])
        if next[0] >= 0 and next[0] < n and next[1] >= 0 and next[1] < m:
            if next not in q and next not in visited:
                if maze[next[0]][next[1]] == "1":
                    q.append(next)
                    depth_chart[next] = depth_chart[curr] + 1

print(depth_chart[dest])