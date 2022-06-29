import sys
from collections import deque

sys.setrecursionlimit(10 ** 4)

input = lambda : sys.stdin.readline().strip()
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

#    위 왼 아래 오
dx = [-1,0,1,0]
dy = [0,-1,0,1]

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == -1:
                continue
            
            if graph[nx][ny] == 0:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1

# 다 돌렸는데 안 익은 토마토가 있을 경우

check = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            check = True
            break
if check:
    print(-1)
else:
    print(max(map(max, graph)) - 1)


'''토마토가 bfs안에서 영향을 줌'''

# visited = [[False for _ in range(m)] for _ in range(n)]
# cnt = 0

# def bfs(row, col):
#     global switch
#     if row < 0 or row >= n or col < 0 or col >= m:
#         return
    
#     if graph[row][col] == -1:
#         return

#     elif graph[row][col] == 0: 
#         graph[row][col] = 1
#         return
    
#     elif graph[row][col] == 1 and visited[row][col] == False:
#         print('들어온 인덱스', row,col)
#         visited[row][col] = True
#         bfs(row+1, col)
#         bfs(row, col+1)
#         bfs(row-1, col)
#         bfs(row, col-1)
        
# def findT(graph):
#     s = []
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 1 and visited[i][j] == False:
#                 s.append((i,j))
                
#     return s
    
# while True:
#     print('들어간다')
#     tmp = 0
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 tmp += 1
#     if tmp != 0:
#         graph_t = deepcopy(graph)
#         for idx in findT(graph):
#             print('들어간 인덱스', idx)
#             bfs(idx[0],idx[1])
#             print(graph)
            
#         if graph_t == graph:
#             break
#         cnt += 1
#     else:
#         break

