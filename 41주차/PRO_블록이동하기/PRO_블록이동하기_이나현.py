#프로그래머스 블록 이동하기
from collections import deque

def solution(board):
    N = len(board)
    visited = dict()
    check_obs_h = [[0,-1],[0,2],[-1,1],[-1,0],[1,1],[1,0]] #좌직, 우직, 좌기준상, 우기준상, 좌기준하, 우기준하
    check_obs_v = [[-1,0],[2,0],[1,-1],[0,-1],[1,1],[0,1]]
    move_h = [[0,-1,0,-1,"h"],[0,1,0,1,"h"],[-1,0,0,-1,"v"],[-1,1,0,0,"v"],[0,0,1,-1,"v"],[0,1,1,0,"v"]]
    move_v = [[-1,0,-1,0,"v"],[1,0,1,0,"v"],[0,-1,-1,0,"h"],[1,-1,0,0,"h"],[0,0,-1,1,"h"],[1,0,0,1,"h"]]
    q = deque([[(0,0),(0,1),0,"h"]]) #pos1, pos2, cnt, h/v
    visited[((0,0),(0,1))] = True
    while q:
        pos1, pos2, cnt, hv = q.popleft()
        if pos1 == (N-1, N-1) or pos2 == (N-1, N-1):
            return cnt
        if hv == "h":
            check_obs = check_obs_h
            move = move_h
        else:
            check_obs = check_obs_v
            move = move_v

        for i in range(6):
            y1, x1 = pos1
            y2, x2 = pos2
            yo, xo = y1+check_obs[i][0], x1+check_obs[i][1]
            if 0 <= yo < N and 0 <= xo < N and board[yo][xo]==0:
                ny1, nx1, ny2, nx2 = y1+move[i][0], x1+move[i][1], y2+move[i][2], x2+move[i][3]
                if all([0<=ny1<N, 0<=nx1<N, 0<=ny2<N, 0<=nx2<N ,board[ny1][nx1]==0, board[ny2][nx2]==0]):
                    if ((ny1,nx1),(ny2,nx2)) not in visited:
                        visited[((ny1,nx1),(ny2,nx2))] = True
                        q.append([(ny1,nx1),(ny2,nx2),cnt+1,move[i][4]])


# print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))