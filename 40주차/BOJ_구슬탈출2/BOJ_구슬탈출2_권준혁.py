from collections import deque
from copy import deepcopy

dx = [1,0,-1,0]
dy = [0,-1,0,1]

dic = {
    0:lambda x:[x[0] + 1, x[1]], # 아래 방향
    1:lambda x:[x[0], x[1] - 1], # 왼쪽 방향
    2:lambda x:[x[0] - 1, x[1]], # 위 방향
    3:lambda x:[x[0], x[1] + 1], # 오른쪽 방향
    }

def check_next_available(board, rr, bb, i):
    nr = [rr[0] + dx[i], rr[1] + dy[i]]
    nb= [bb[0] + dx[i], bb[1] + dy[i]]
    return True if board[nr[0]][nr[1]] != '#' or board[nb[0]][nb[1]] != '#' else False

def check_first(rr, bb, i):
    if i == 0: # 아래 방향
        return True if rr[0] >= bb[0] else False
    elif i == 1: # 왼쪽 방향
        return True if rr[1] <= bb[1] else False
    elif i == 2: # 위 방향
        return True if rr[0] <= bb[0] else False
    elif i == 3: # 오른쪽 방향
        return True if rr[1] >= bb[1] else False

def move(board, loc, i, letter):

    def check(board, nx, ny, letter):
        convert = {'B':'R', 'R':'B'}
        if board[nx][ny] == '.' or board[nx][ny] == 'O':
            return [nx, ny]
        elif board[nx][ny] == '#' or board[nx][ny] == convert[letter]:
            return None
    
    while(1):
        nx, ny = dic[i](loc)
        if check(board, nx, ny, letter) != None:
            loc = [nx, ny]
            if board[nx][ny] == 'O':
                break
        else:
            break
    return loc

def refresh_board(board, next_loc, loc, letter):
    # print(next_loc, loc)
    board[loc[0]][loc[1]] = '.'
    if board[next_loc[0]][next_loc[1]] == 'O':
        pass # letter 사라짐
    else:
        board[next_loc[0]][next_loc[1]] = letter
    return board

def get_next(board, rr, bb, i):
    if check_first(rr, bb,  i): # if True: move red first
        next_r = move(board, rr, i, 'R')
        # if rr == [3, 5] and i == 2:
            # breakpoint()
        board = refresh_board(board, next_r, rr, 'R')
        next_b = move(board, bb, i, 'B')
        board = refresh_board(board, next_b, bb, 'B')
    else:
        next_b = move(board, bb, i, 'B')
        board = refresh_board(board, next_b, bb, 'B')
        next_r = move(board, rr, i, 'R')
        board = refresh_board(board, next_r, rr, 'R')
    return next_r, next_b, board

def check_finish(nr, nb, hole):
    if nb == hole: # 블루가 구멍으로 빠진 상태
        return 2
    elif nr == hole:
        return 1
    else:
        return 0

def print_board(board):
    for i in range(len(board)):
        print(board[i])
    print("-------------------")

def run(board, r, b, hole): # h: hole
    q = deque([[r, b, 0, board]])
    while(q):
        rr, bb, cc, cboard = q.popleft() # cc: depth
        if cc > 10:
            return -1
        for i in range(4):
            if check_next_available(cboard, rr, bb, i):
                nr, nb, next_cboard = get_next(deepcopy(cboard), rr, bb, i)
                state = check_finish(nr, nb, hole)
                if state == 2: # 블루가 hole로 들어간 경우 (게임 종료)
                    continue
                elif state == 1: # 게임 종료
                    return cc + 1
                elif state == 0:  # 게임 계속 진행
                    q.append([nr, nb, cc + 1, next_cboard])
    return -1

def get_loc(board:list):
    r, b, h = 0, 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                r = [i, j]
            elif board[i][j] == 'B':
                b = [i, j]
            elif board[i][j] == 'O':
                h = [i, j]
    return r, b, h

if __name__ == '__main__':
    global answer
    answer = float('inf')
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    rloc, bloc, hloc = get_loc(board)
    answer = run(board, rloc, bloc, hloc)
    print(answer if answer <= 10 else -1)