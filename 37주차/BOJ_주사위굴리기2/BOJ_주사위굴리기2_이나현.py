#보드 스코어링 : bfs로 보드스코어링을 미리 해준 후 주사위가 해당 위치에 가면 answer에 해당 위치값을 더해준다.
#주사위 굴리기 : 주사위 전개도를 바닥을 중심으로 3x3으로 표현, 나머지는 top 위치가 된다.
#             top 위치는 전개도의 동서남북 어디든 붙일 수 있다.

from collections import deque
import copy

#보드 점수화하기
def score_board(board):
    board = copy.deepcopy(board)
    visited = [[False]*M for _ in range(N)]
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            visited[i][j] = True
            value = board[i][j]
            same_value_pos = [[i,j]]
            q = deque([[i,j]])
            cnt = 1
            while q:
                ci, cj = q.popleft()
                for di, dj in direction:
                    ni, nj = ci+di, cj+dj
                    if not (0<=ni<N and 0<=nj<M) or visited[ni][nj]:
                        continue
                    if board[ni][nj] == value:
                        visited[ni][nj] = True
                        same_value_pos.append([ni,nj])
                        q.append([ni,nj])
                        cnt += 1
            for pos in same_value_pos:
                board[pos[0]][pos[1]] = value * cnt
    return board

#주사위 굴리기
def roll_dice():
    global top
    if d == 0:   #굴리고자하는 방향이 동
        ntop = dice[1][0]
        dice[1][0], dice[1][1], dice[1][2] = dice[1][1], dice[1][2], top
        top = ntop
    elif d == 1: #굴리고자하는 방향이 남
        ntop = dice[0][1]
        dice[0][1], dice[1][1], dice[2][1] = dice[1][1], dice[2][1], top
        top = ntop
    elif d == 2: #굴리고자하는 방향이 서
        ntop = dice[1][2]
        dice[1][1], dice[1][2], dice[1][0] = dice[1][0], dice[1][1], top
        top = ntop
    else:        #굴리고자하는 방향이 북
        ntop = dice[2][1]
        dice[0][1], dice[1][1], dice[2][1] = top, dice[0][1], dice[1][1]
        top = ntop


N, M, move_cnt = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
s_board = score_board(board)
dice = [[0]*3 for _ in range(3)]
dice[0][1], dice[1][0], dice[1][1], dice[1][2], dice[2][1], top = 2,4,6,3,5,1 #바닥을 기준으로 북,서,자신,동,남,top
direction = [[0,1],[1,0],[0,-1],[-1,0]] #동, 남, 서, 북
d = 0
answer = 0
ci, cj = 0,0
for cnt in range(move_cnt):
    ci += direction[d][0]
    cj += direction[d][1]
    
    if not (0<=ci<N and 0<=cj<M): #현재 위치가 보드밖인 경우
        d = (d+2)%4
        ci += direction[d][0] * 2
        cj += direction[d][1] * 2

    answer += s_board[ci][cj]
    roll_dice()
    bottom_value = dice[1][1]
    board_value = board[ci][cj]
    if bottom_value > board_value:
        d = (d+1)%4
    elif bottom_value < board_value:
        d = (d-1)%4
print(answer)