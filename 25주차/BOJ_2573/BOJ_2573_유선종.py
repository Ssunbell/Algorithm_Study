import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n, m  = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
melting_list = deque(sorted([(i,j) for i in range(n) for j in range(m) if graph[i][j]]))
####  북 남 동 서
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
k = 3
while k:
    visited = [[0 for _ in range(m)] for _ in range(n)]

    del_list = []
    group = 0
    # dp에 녹은 빙산 갯수 저장
    for index in melting_list:
        i, j = index
        if not visited[i][j]:
            print('들어감')
            q = deque([[i, j]])
            visited[i][j] = 1
            melting = []
            
            while q:
                print(q)
                x, y = q.popleft()
                melt = 0
                for idx in range(4):
                    nx = x + dx[idx]
                    ny = y + dy[idx]
                    if 0 <= x < n and 0 <= y < m:
                        if not graph[nx][ny]:
                            melt += 1
                        elif graph[nx][ny] and not visited[nx][ny]:
                            q.append([nx, ny])
                            visited[nx][ny] = 1
                            
                if melt:
                    melting.append((x,y,melt))
            print('melting', melting)
            for row, col, melt in melting:
                graph[row][col] = max(0, graph[row][col] - melt)
                if not graph[row][col]:
                    del_list.append((row,col))
            group += 1
            
    print(group)
    for lsm in graph:
        print(lsm)
    print(melting_list)
    print(del_list)
    for d in del_list:
        melting_list.remove(d)
        
    if group > 1:
        print(answer)
        break
    
    answer += 1
    k-=1
    
if group < 2:
    print(0)