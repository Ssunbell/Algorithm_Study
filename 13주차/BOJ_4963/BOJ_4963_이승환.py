import sys
from collections import deque

while True:
    input_s = lambda : sys.stdin.readline().strip()
    w, h = map(int, input_s().split())

    if w == 0 and h == 0:
        break

    m = deque()
    for _ in range(h):
        m.append(list(map(int,input_s().split())))

    visited = deque()
    q = deque()
    dx = [1,1,-1,-1,1,0,-1,0]
    dy = [1,-1,-1,1,0,1,0,-1]
    cnt = 0

    for x in range(h):
        for y in range(w):
            if m[x][y] == 1 and (x,y) not in visited:
                q.append((x,y))
                cnt += 1

                while q:
                    curr = q.popleft()
                    visited.append(curr)

                    for i in range(8):
                        next = (curr[0]+dx[i],curr[1]+dy[i])
                        if next[0] < 0 or next[0] >= h or next[1] < 0 or next[1] >= w:
                            continue
                        if m[next[0]][next[1]] == 1 and next not in visited and next not in q:
                            q.append(next)
    print(cnt)