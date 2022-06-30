import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()

n,m = map(int, input().split())

maze = [list(map(int, input())) for _ in range(n)]

q = deque()
q.append((0,0))
#    아래, 오, 위, 왼 시작점이 (0,0)이므로 아래/오른쪽부터 탐색하도록 설정
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == 0:
                continue
            
            if maze[nx][ny] == 1:
                q.append((nx,ny))
                maze[nx][ny] = maze[x][y]+1

print(maze[n-1][m-1])