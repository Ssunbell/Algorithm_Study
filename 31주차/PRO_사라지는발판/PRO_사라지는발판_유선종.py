# 밟고 있는 발판에서 발을 떼면 해당 발판이 사라짐
# 1. 더이상 움직일 수 없을 경우
# 2. 같은 발판을 밟고 있을 때, 상대방이 먼저 움직일 경우
# 최대한 오래 버틴다는 것은 양 플레이어가 캐릭터를 움직이는 횟수를 최대화

def qwer(board, loc):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    position = []
    for i in range(4):
        nx = loc[0] + dx[i]
        ny = loc[1] + dy[i]
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 1:
            position.append((nx,ny))
            
    return position

def bfs(board, aloc, bloc, turn):
    # 이동 가능한 좌표를 반환
    # 움직이지 않았을 경우 0을 반환하기 위해 turn은 0부터 시작
    A_turn = turn % 2 == 0 # A_turn이 True일 경우 A_turn
    if A_turn: # A turn
        position = qwer(board, aloc)
    else: # B turn
        position = qwer(board, bloc)
    
    # 이동이 불가능하거나 둘이 같은 좌표에 서있게 되면 게임 종료
    if not position:
        return not A_turn, turn # positioin이 없으면 A가 진 경기이므로 not A_turn으로 졌다는 것을 표시
    if aloc == bloc:
        return A_turn, turn + 1
    
    win, lose = [], []
    if A_turn:
        board[aloc[0]][aloc[1]] = 0
        for nx, ny in position:
            A_win, cnt = bfs(board, [nx, ny], bloc, turn + 1)
            if A_win:
                win.append(cnt)
            else:
                lose.append(cnt)
        board[aloc[0]][aloc[1]] = 1
    else:
        board[bloc[0]][bloc[1]] = 0
        for nx, ny in position:
            A_win, cnt = bfs(board, aloc, [nx, ny], turn + 1)
            if A_win:
                lose.append(cnt)
            else:
                win.append(cnt)
        board[bloc[0]][bloc[1]] = 1
    
    # 백트래킹을 다 돌고 나서 마지막에 win, lose가 최신화됨
    if win:
        return A_turn, min(win)
    else:
        return not A_turn, max(lose)

def solution(board, aloc, bloc):
    _, answer = bfs(board, aloc, bloc, 0)
    
    return answer