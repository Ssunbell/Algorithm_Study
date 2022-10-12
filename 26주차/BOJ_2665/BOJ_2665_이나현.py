#[미로만들기]
from collections import deque
def bfs(cnt, now):
    global N
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    next = deque()
    while now:
        oi, oj = now.popleft()
        for k in range(4):
            ni = oi + di[k]
            nj = oj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False:
                if ni == N-1 and nj == N-1:
                    wall_cnt[ni][nj] = cnt
                    return
                visited[ni][nj] = True
                if table[ni][nj] == 1:
                    wall_cnt[ni][nj] = cnt
                    now.append([ni, nj])
                else:
                    wall_cnt[ni][nj] = wall_cnt[oi][oj] + 1
                    next.append([ni, nj])
    bfs(cnt+1, next)

N = int(input())
table = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
visited[0][0] = True
wall_cnt = [[-1] * N for _ in range(N)]
wall_cnt[0][0] = 0
que = deque([[0, 0]])
bfs(0, que)
print(wall_cnt[N-1][N-1])