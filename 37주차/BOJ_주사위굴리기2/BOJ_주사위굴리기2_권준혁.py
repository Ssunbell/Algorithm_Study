from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def check_avilable(n, m, loc, dir):
    if dir == 0: # 동쪽
        next_loc = [loc[0], loc[1] + 1]
        opposite_loc = [loc[0], loc[1] - 1]
    elif dir == 1: # 서쪽
        next_loc = [loc[0], loc[1] - 1]
        opposite_loc = [loc[0], loc[1] + 1]
    elif dir == 2: # 남쪽
        next_loc = [loc[0] + 1, loc[1]]
        opposite_loc = [loc[0] - 1, loc[1]]
    elif dir == 3: # 북쪽
        next_loc = [loc[0] - 1, loc[1]]
        opposite_loc = [loc[0] + 1, loc[1]]
    return (True, next_loc) if 0 <= next_loc[0] < n and 0 <= next_loc[1] < m else (False, opposite_loc)

def get_score(board, loc, dir, dice):
    b = board[loc[0]][loc[1]] # 주사위가 도착한 칸의 값
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    visited[loc[0]][loc[1]] = True
    q = deque([loc])
    c = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < len(board) and 0 <= yy < len(board[0]) and board[xx][yy] == b and not visited[xx][yy]:
                c += 1
                visited[xx][yy] = True
                q.append((xx, yy))
    return b * c

def get_next_dir(board, loc, dir, dice):
    a = dice[3]
    b = board[loc[0]][loc[1]]
    if a > b:
        dic = {0:2, 2:1, 1:3, 3:0}
        dir = dic[dir]
    elif a < b:
        dic = {0:3, 3:1, 1:2, 2:0}
        dir = dic[dir]
    return dir

def rotate_dice(dice, dir):
    if dir == 0:
        dice[1][1], dice[1][2], dice[3], dice[1][0] = dice[1][0], dice[1][1], dice[1][2], dice[3]
    elif dir == 1:
        dice[3], dice[1][0], dice[1][1], dice[1][2] = dice[1][0], dice[1][1], dice[1][2], dice[3]
    elif dir == 2:
        dice[1][1], dice[2][1], dice[3], dice[0][1] = dice[0][1], dice[1][1], dice[2][1], dice[3]
    elif dir == 3:
        dice[3], dice[0][1], dice[1][1], dice[2][1] = dice[0][1], dice[1][1], dice[2][1], dice[3]
    return dice

def print_dice(dice):
    for i, d in enumerate(dice):
        if i == len(dice) - 1:
            print('%5d' % d)
        else:
            print(d)

if __name__ == '__main__':
    answer = 0
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], 6]
    loc = [0, 0]
    dir = 0
    change_dir = {0:1, 1:0, 2:3, 3:2}
    while(k):
        check, loc = check_avilable(n, m, loc, dir)
        if not check:
            dir = change_dir[dir]
        dice = rotate_dice(dice, dir)
        answer += get_score(board, loc, dir, dice)
        dir = get_next_dir(board, loc, dir, dice)
        k -= 1
    print(answer)