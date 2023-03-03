from collections import deque

move = [(1,0,"d"), (0,-1,"l"), (0,1,"r"), (-1,0,"u")]
dist = lambda x,y,r,c : abs(x-r)+abs(y-c)

def solution(n, m, x, y, r, c, k):
    q = deque()
    q.append((0, "", x, y))
    if dist(x,y,r,c) > k or (k-dist(x,y,r,c))%2==1:
        return "impossible"
    
    while q:
        move_cnt, cmd, cx, cy = q.popleft()
        if cx == r and cy == c and move_cnt == k:
            return cmd
        for dx, dy, direction in move:
            nx, ny = dx+cx, dy+cy
            if 0<nx<=n and 0<ny<=m and move_cnt < k:
                if dist(nx,ny,r,c) > k-move_cnt: continue
                q.append((move_cnt+1, cmd+direction, nx, ny))
    return "impossible"

tc = [
    [3,	4,	2,	3,	3,	1,	5, "dllrl"],
    [2,	2,	1,	1,	2,	2,	2, "dr"],
    [3,	3,	1,	2,	3,	3,	4, "impossible"],
]
for c in tc:
    print(solution(*c[:-1]), c[-1])