from collections import deque
dx = [1,0,-1,0]
dy = [0,-1,0,1]

def get_near(board:list, location:tuple):
    (cx, cy), n = location, len(board)
    for direction, i in enumerate(range(4)):
        nx, ny = cx+dx[i], cy+dy[i]
        if (0<=nx<n) and (0<=ny<n) and (board[ny][nx]==0):
            yield (nx, ny), direction

            
def solution(board):
    n = len(board)
    shortest_fee = [[[float("inf")]*4 for _ in range(n)]for _ in range(n)]
    q = deque([(0, (0,0),-1)])
    
    while q:
        fee, loc, direction = q.popleft()
        for nloc, ndirection in get_near(board, loc):
            nx, ny = nloc
            nfee = fee + (100 if ndirection == direction else 600)
            if shortest_fee[ny][nx][ndirection] <= nfee:
                continue
            q.append((nfee, nloc, ndirection))
            shortest_fee[ny][nx][ndirection] = nfee
    return min(shortest_fee[n-1][n-1])-500