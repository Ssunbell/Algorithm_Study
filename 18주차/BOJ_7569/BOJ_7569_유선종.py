import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
m, n, h = map(int, input().split()) # 열, 행, 높이
tomato_box = []
q = deque([])
for z in range(h):
    tmp = []
    for i in range(n):
        tmp.append(list(map(int, input().split())))
        for j in range(m):
            if tmp[i][j] == 1:
              q.append((z,i,j))  
    tomato_box.append(tmp)

#    앞 왼 뒤 오 위 아래
dz = [0,0,0,0,1,-1]
dx = [-1,0,1,0,0,0]
dy = [0,-1,0,1,0,0]

while q:
    z,x,y = q.popleft()
    for i in range(6):
        nz = z+dz[i]
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomato_box[nz][nx][ny] == 0:
            q.append((nz,nx,ny))
            tomato_box[nz][nx][ny] = tomato_box[z][x][y]+1
answer = 0
for z in range(h):
    for i in range(n):
        for j in range(m):
            if tomato_box[z][i][j]==0:
                print(-1)
                exit(0)
            answer = max(answer, tomato_box[z][i][j])
print(answer-1)