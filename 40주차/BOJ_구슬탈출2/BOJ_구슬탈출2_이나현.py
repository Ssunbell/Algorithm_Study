#백준 13460 구슬탈출2
#bfs, 구현
#주의 point
#구슬을 굴릴 때, 방향에 따라 어느 구슬을 먼저 굴릴지 고려해야함 ex) 왼쪽으로 굴릴 떄 파란구슬이 빨간구슬보다 왼쪽 -> 파란구슬 먼저 굴리기
#빨간구슬이 탈출 후 파란구슬도 탈출 가능한지 확인해야함 -> 빨간구슬 탈출했다면, 파란구슬도 같은 방향으로 한번 더 굴려서 탈출 확인

from collections import deque

def move_red(cx, cy, bx, by, d):
    fx = cx + dx[d]
    fy = cy + dy[d]
    while board[fx][fy] == '.' or board[fx][fy] == 'O':
        if fx == bx and fy == by: # 파란공과 같은 위치 안됨
            return [cx, cy]
        cx = fx
        cy = fy
        if board[cx][cy] == 'O':
            return [cx, cy]
        fx = cx + dx[d]
        fy = cy + dy[d]
    return [cx, cy]


def move_blue(cx, cy, rx, ry, d):
    fx = cx + dx[d]
    fy = cy + dy[d]
    while board[fx][fy] == '.' or board[fx][fy] == 'O':
        if fx == rx and fy == ry: #빨간공과 같은 위치 안됨
            return [cx, cy]
        cx = fx
        cy = fy
        if board[cx][cy] == 'O':
            return [cx, cy]
        fx = cx + dx[d]
        fy = cy + dy[d]
    return [cx, cy]


def red_first(rx, ry, bx, by, d):
    if d == 0: #상
        return True if rx <= bx else False
    elif d == 1: #하
        return True if rx >= bx else False
    elif d == 2: #좌
        return True if ry <= by else False
    else: #우
        return True if ry >= by else False


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(1, N):
    for j in range(1, M):
        if board[i][j] == 'R':
            red_pos = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'B':
            blue_pos = [i, j]
            board[i][j] = '.'

q = deque([[*red_pos, *blue_pos, 1]])
ds = deque([2, 1, 3, 1, 2])
while q:
    rx, ry, bx, by, cnt = q.popleft()
    if cnt > 10:
        break
    for d in range(4):
        if red_first(rx, ry, bx, by, d):
            frx, fry = move_red(rx, ry, bx, by, d)
            fbx, fby = move_blue(bx, by, frx, fry, d)
        else:
            fbx, fby = move_blue(bx, by, rx, ry, d)
            frx, fry = move_red(rx, ry, fbx, fby, d)
        if rx == frx and ry == fry and bx == fbx and by == fby: # 안움직
            continue
        if board[frx][fry] == 'O':
            frx, fry = 0, 0
            fbx, fby = move_blue(bx, by, frx, fry, d)
            if board[fbx][fby] == 'O':
                continue
            else:
                print(cnt)
                exit()
        if board[fbx][fby] == 'O':
                continue
        q.append([frx, fry, fbx, fby, cnt + 1])
print(-1)