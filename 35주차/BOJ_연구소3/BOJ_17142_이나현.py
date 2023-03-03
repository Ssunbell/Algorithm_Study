#[연구소 3] 80점
from itertools import combinations
from collections import deque
import copy

def bfs(board, N, case):
    q = deque()
    move = [(-1,0),(1,0),(0,-1),(0,1)]          #상하좌우
    visited = [[False] * N for _ in range(N)]
    for r, c in case:
        q.append((0, r, c))
    while q:
        time, r, c = q.popleft()
        if visited[r][c]: continue
        visited[r][c] = True
        for h, v in move:
            nr = r + h
            nc = c + v
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
                board[nr][nc] = board[r][c] + 1
                q.append((board[nr][nc], nr, nc))
    res = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return 1e9
            res = max(res, board[i][j])
    return res - 2



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
location = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            location.append((i,j))
cases = list(combinations(location, M))
result = 1e9
for case in cases:
    board_copy = copy.deepcopy(board)
    time = bfs(board_copy, N, case)
    result = min(result, time)

print(result if result < 1e9 else -1)