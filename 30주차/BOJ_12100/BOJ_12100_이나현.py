#12100_2046(Easy)
from itertools import product
import copy

def move_up(board, n):
    for j in range(n):
        top = 0
        for i in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[top][j] == 0:
                    board[top][j] = tmp
                elif board[top][j] == tmp:
                    board[top][j] = tmp * 2
                    top += 1
                else:
                    top += 1
                    board[top][j] = tmp
    return board

def move_down(board, n):
    for j in range(n):
        top = n - 1
        for i in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[top][j] == 0:
                    board[top][j] = tmp
                elif board[top][j] == tmp:
                    board[top][j] = tmp * 2
                    top -= 1
                else:
                    top -= 1
                    board[top][j] = tmp
    return board

def move_left(board, n):
    for i in range(n):
        top = n - 1
        for j in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][top] == 0:
                    board[i][top] = tmp
                elif board[i][top] == tmp:
                    board[i][top] = tmp * 2
                    top -= 1
                else:
                    top -= 1
                    board[i][top] = tmp
    return board

def move_right(board, n):
    for i in range(n):
        top = 0
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][top] == 0:
                    board[i][top] = tmp
                elif board[i][top] == tmp:
                    board[i][top] = tmp * 2
                    top += 1
                else:
                    top += 1
                    board[i][top] = tmp
    return board


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
move = ['상','하','좌','우']
result = 0
for case in product(move, repeat=5):
    copied = copy.deepcopy(board)
    for t in range(5):
        if case[t] == '상':
            copied = move_up(copied, N)
        elif case[t] == '하':
            copied = move_down(copied, N)
        elif case[t] == '좌':
            copied = move_left(copied, N)
        else:
            copied = move_right(copied, N)
    max_num = 0
    for i in range(N):
        for j in range(N):
            max_num = max(max_num, copied[i][j])
    result = max(result, max_num)
print(result)