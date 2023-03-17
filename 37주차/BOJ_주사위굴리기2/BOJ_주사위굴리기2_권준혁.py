def check_avilable(n, m, loc, dir):
    if dir == 0: # 동쪽
        next_loc = [loc[0], loc[1] + 1]
        opposite_loc = [loc[0], loc[1] - 1]
    elif dir == 1:
        next_loc = [loc[0], loc[1] - 1]
        opposite_loc = [loc[0], loc[1] + 1]
    elif dir == 2:
        next_loc = [loc[0] - 1, loc[1]]
        opposite_loc = [loc[0] + 1, loc[1]]
    elif dir == 3:
        next_loc = [loc[0] + 1, loc[1]]
        opposite_loc = [loc[0] - 1, loc[1]]
    return True, next_loc if next_loc[0] < n and next_loc[1] < m else False, opposite_loc

def get_score(board, loc, dir, dice):
    a = dice[1] # 아랫면의 정수
    b = board[loc[0]][loc[1]] # 주사위가 도착한 칸의 값

def get_next_dir(board, loc, dir, dice):
    pass

if __name__ == '__main__':
    answer = 0
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dice = [1, 2, 3, 4, 5, 6]
    loc = [0, 0]
    dir = 0
    change_dir = {0:1, 1:0, 2:3, 3:2}
    while(k):
        check, loc = check_avilable(n, m, loc, dir)
        if not check:
            dir = change_dir[dir]
        answer += get_score(board, loc, dir, dice)
        dir = get_next_dir(board, loc, dir, dice)
        k -= 1
    print(answer)