import sys
sys.setrecursionlimit(10**6)
dx = [0,0,1,-1]
dy = [-1,1,0,0]

round_player = lambda x:x%2

def isin_grid(board, loc):
    return 0<=loc[0]<len(board[0]) and 0<=loc[1]<len(board)

def get_near(board, loc):
    for i in range(4):
        nx, ny = loc[0] + dx[i], loc[1] + dy[i]
        if not isin_grid(board, (nx,ny)):
            continue
        if board[ny][nx]:
            yield (nx,ny)


def btk(board, loc1, loc2, round):
    # determine current player
    move = get_near(board, loc1)
    
    # endsetup
    if not move:
        return False, 0
    if loc1==loc2:
        return True, 1
    
    # btk
    min_round, max_round = 10**10, 0
    win = False
    for ncoord in move:
        board[loc1[1]][loc1[0]]=0
        canwin, cnt = btk(board, loc2, loc1, round+1)
        board[loc2[1]][loc1[0]]=1
        if canwin:
            max_round = max(max_round, cnt)
        else:
            win=True
            min_round = min(min_round, cnt)
    nturn = min_round if win else max_round
    return win, nturn

def solution(board, aloc, bloc):
    aloc = (aloc[1], aloc[0])
    bloc = (bloc[1], bloc[0])
    return btk(board, aloc, bloc, 0)[1]



tc = [
    [[[1, 1, 1], [1, 1, 1], [1, 1, 1]],	[1, 0],	[1, 2],	5],
    [[[1, 1, 1], [1, 0, 1], [1, 1, 1]],	[1, 0],	[1, 2],	4],
    [[[1, 1, 1, 1, 1]],	[0, 0],	[0, 4],	4],
    [[[1]],	[0, 0],	[0, 0],	0],
]

if __name__ == "__main__":
    for c in tc:
        # print(solution(*c[:-1]), c[-1], solution(*c[:-1]) == c[-1])
        print(solution(*c[:-1]))