from copy import deepcopy

def canMove(board, loc):
    r, c = loc
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if ((0 <= nr < len(board)) and (0 <= nc < len(board[0]))) and (board[nr][nc] == 1):
            return True
    return False

def search(board, aloc, bloc, step):
    r, c = aloc if step % 2 == 0 else bloc
    if canMove(board, [r,c]) == False:
    	return (False, 0)      # 움직임이 불가능할 경우
    if aloc == bloc:
    	return (True, 1)                         # 같은 위치에 있는 경우

    nboard = deepcopy(board)
    nboard[r][c] = 0
    canWin = False
    maxTurn, minTurn = 0, float('inf')
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    for i in range(4):  # 하, 상, 우, 좌
        nr, nc = r + dx[i], c + dy[i]
        if ((0 <= nr < len(board)) and (0 <= nc < len(board[0]))) and (nboard[nr][nc] == 1):
            if step % 2 == 0:                                       # DFS
                res = search(nboard, [nr, nc], bloc, step+1)    # 다음 B의 차례
            else:
                res = search(nboard, aloc, [nr, nc], step+1)    # 다음 A의 차례

            if res[0]==False:   # 상대가 지면 나는 이기는 경우
                canWin = True
                minTurn = min(minTurn, res[1])
            else:               # 상대가 이기면 나는 지는 경우
                maxTurn = max(maxTurn, res[1])

    if canWin==True:                # 이기는 경우에
        return (canWin, minTurn+1)  # 최소의 움직임 반환
    else:                           # 지는 경우에
        return (canWin, maxTurn+1)  # 최대의 움직임 반환

def solution(board, aloc, bloc):
    answer = search(board, aloc, bloc, 0)
    return answer[1]