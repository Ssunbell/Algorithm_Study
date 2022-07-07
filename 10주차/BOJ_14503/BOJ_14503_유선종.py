import sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int,input().split())
r, c, d = map(int, input().split())

# n by m 행렬
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

#인덱스 북  동  남  서
dx = [-1, 0, 1, 0]# 행
dy = [0, 1, 0, -1]# 열

answer = 0
def clean(r, c, d):
    global answer
    if room[r][c] == 0:
        room[r][c] = 2
        for i in room:
            print(*i)
        answer += 1
        
    for _ in range(4):
        nd = (d + 3) % 4
        nx = r + dx[nd]
        ny = c + dy[nd]
        if room[nx][ny] == 0:
            clean(nx, ny, nd)

            return
        d = nd
    nd = (d + 2) % 4
    nx = r + dx[nd]
    ny = c + dy[nd]
    if room[nx][ny] == 1:
        return
    clean(nx, ny, d)
    
clean(r, c, d)
print(answer)