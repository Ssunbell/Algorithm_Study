#백준 20062 모노미노도미노2
#파란색과 초록색 보드에 블럭을 놓고, 스코어 계산, 특별 행 처리 순으로 진행
#파란색 보드를 행과 열을 바꿔서 구현
#deque의 pop과 appendleft를 통해 보드를 한칸씩 이동하는 것을 구현

from collections import deque

def place_block(t, x, y):
    if t == 1:
        bi, gi = 0, 0
        while bi < 5 and blue_board[bi+1][x] == False: bi += 1
        blue_board[bi][x] = True

        while gi < 5 and green_board[gi+1][y] == False: gi += 1
        green_board[gi][y] = True
    elif t == 2:
        bi, gi = 0, 0
        while bi < 4 and blue_board[bi+2][x] == False: bi += 1
        blue_board[bi][x] = True
        blue_board[bi+1][x] = True
        
        while gi < 5 and green_board[gi+1][y] == False and green_board[gi+1][y+1] == False: gi += 1
        green_board[gi][y] = True
        green_board[gi][y+1] = True
    else:
        bi, gi = 0, 0
        while bi < 5 and blue_board[bi+1][x] == False and blue_board[bi+1][x+1] == False: bi += 1
        blue_board[bi][x] = True
        blue_board[bi][x+1] = True

        while gi < 4 and green_board[gi+2][y] == False: gi += 1
        green_board[gi][y] = True
        green_board[gi+1][y] = True


def calculate_boards():
    global score
    for i in range(6):
        if all(blue_board[i]):
            score += 1
            del blue_board[i]
            blue_board.appendleft([False]*4)
    for i in range(6):
        if all(green_board[i]):
            score += 1
            del green_board[i]
            green_board.appendleft([False]*4)
    

def check_special_line():
    for i in range(2):
        if any(blue_board[i]):
            blue_board.pop()
            blue_board.appendleft([False]*4)
    for i in range(2):
        if any(green_board[i]):
            green_board.pop()
            green_board.appendleft([False]*4)


N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]
blue_board = deque([[False]*4 for _ in range(6)])
green_board = deque([[False]*4 for _ in range(6)])
score = 0
for block in blocks:
    t, x, y = block
    place_block(t, x, y)
    calculate_boards()
    check_special_line()
print(score)
cnt = 0
for row in blue_board:
    cnt += sum(row)
for row in green_board:
    cnt += sum(row)
print(cnt)