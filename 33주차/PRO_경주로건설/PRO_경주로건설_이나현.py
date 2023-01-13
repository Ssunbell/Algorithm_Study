#[프로그래머스_경주로건설]
#bfs, 다이나믹
#96점
from collections import deque
def solution(board):
    n = len(board)
    board_cost = [[320_000]*n for _ in range(n)] # 25x25x500 = 312500
    board_cost[0][0] = 0
    dx, dy = [-1,0,1,0], [0,1,0,-1] #상우하좌
    que = deque()
    que.append([0,0,0,0])
    
    while que:
        x, y, past_k, past_cost = que.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if x==0 and y==0:
                cost = 100
            else:
                cost = past_cost + (100 if past_k == k else 600)
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                if (cost <= board_cost[nx][ny]):
                    que.append([nx, ny, k, cost])
                    board_cost[nx][ny] = cost
    return board_cost[n-1][n-1]



# 72점 코드
# 위 코드와의 차이점 : cost를 que에 안넣어줬다.
# 단순히 그 위치에서의 최소 비용을 저장하면 안되고 그 위치에서 방향별 최소비용을 저장할 수 있도록 해야한다.
'''
def solution(board):
    n = len(board)
    board_cost = [[320_000]*n for _ in range(n)] # 25x25x500 = 312500
    board_visited = [[0]*n for _ in range(n)]    # 해당 방향 방문했는지 확인용(비트마스킹)
    board_cost[0][0] = 0
    dx, dy = [-1,0,1,0], [0,1,0,-1] #상우하좌
    que = deque()
    que.append([0,0,0])
    
    while que:
        x, y, past_k = que.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if x==0 and y==0:
                cost = 100
            else:
                cost = board_cost[x][y] + (100 if past_k == k else 600)
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                if (cost <= board_cost[nx][ny]):# or not(board_visited[nx][ny] & (1<<k)) :
                    que.append([nx, ny, k])
                    # board_visited[x][y] |= 1<<((k+2)%4)
                    # board_visited[nx][ny] |= 1<<k
                    board_cost[nx][ny] = min(board_cost[nx][ny], cost)
    return board_cost[n-1][n-1]
'''

print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])) 
print(solution(	[[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print(solution(	[[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))

#900, 2100, 3200, 3800