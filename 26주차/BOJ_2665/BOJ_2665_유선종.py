import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def arrow_keys():
    yield 1, 0
    yield 0, 1
    yield -1, 0
    yield 0, -1
    
def bfs(x, y, n):
    q = deque([])
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        
        if x == n-1 and y == n-1:
            return visited[x][y]
        
        for arrow in arrow_keys():
            nx = x + arrow[0]
            ny = y + arrow[1]
            
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 1:
                        q.appendleft((nx,ny))
                        visited[nx][ny] = visited[x][y]
                    else:
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1
        for row in visited:
            print(row)

n = int(input())
graph = [list(map(int,input()[:n])) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

print(bfs(0,0,n) - 1)


# def bfs(graph, x, y, n, count=0):
#     q = deque([])
#     q.append((x,y))
#     visited[x][y] = 1
#     visitied_dict = {}
#     while q:
#         x, y = q.pop()
#         print('x,y', x,y)
#         for arrow in arrow_keys():
#             nx = x + arrow[0]
#             ny = y + arrow[1]
#             if 0<=nx<n and 0<=ny<n and graph[nx][ny]:
#                 if not visited[nx][ny]:
#                     visited[nx][ny] += visited[x][y] + 1
#                     q.append((nx,ny))
                    
#                     if nx != n-1 and ny != n-1:
#                         if visited[nx][ny] not in visitied_dict:
#                             visitied_dict[visited[nx][ny]] = [(nx, ny)]
#                         else:
#                             visitied_dict[visited[nx][ny]].append((nx,ny))
                        
#     for row in visited:
#         print(row)
    
#     count += 1
#     if visitied_dict:
#         for pos in visitied_dict[max(visitied_dict)]:
#             row, col = pos[0], pos[1]
#             if row == (n-1) and col == (n-1):
#                 print('마지막 도착했다.')
#                 counts.append(count)
#                 return
#             for arrow in arrow_keys():
#                 if graph[row+arrow[0]][col+arrow[1]] == 0:
#                     print('들어간다.', row, col)
#                     graph2 = deepcopy(graph)
#                     graph2[row+arrow[0]][col+arrow[1]] = 1
#                     bfs(graph2, row, col, n)