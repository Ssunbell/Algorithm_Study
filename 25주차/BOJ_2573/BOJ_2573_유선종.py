import sys
from collections import deque
# 함수형으로 작성하니까 시간초과 안남

input = lambda: sys.stdin.readline().strip()

n, m  = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
melting_list = deque(sorted([(i,j) for i in range(n) for j in range(m) if graph[i][j]]))
####  북 남 동 서
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

## 이걸 함수로 만들면 쪼끔 나아지긴 함
def melting_ice(melting: list):
    for m in melting:
        row, col, melt = m
        graph[row][col] = max(0, graph[row][col] - melt)
        if not graph[row][col]:
            del_list.append((row, col))

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    melting = []
    
    while q: # bfs 시작
        x, y = q.popleft()
        melt = 0
        for idx in range(4): # 방향 탐색
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= x < n and 0 <= y < m:
                if not graph[nx][ny]:
                    melt += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    
        if melt:
            melting.append((x, y, melt))
    
    melting_ice(melting)

answer = 0
while melting_list:
    visited = deque([[0 for _ in range(m)] for _ in range(n)])

    del_list = deque([])
    group = 0
    for i, j in melting_list:
        if not visited[i][j]:
            bfs(i,j)
            group += 1
            
    if group > 1:
        print(answer)
        break

    for d in del_list:
        melting_list.remove(d)
    
    answer += 1
    
if group < 2:
    print(0)