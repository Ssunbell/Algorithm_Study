'''
아이디어 : 
완전 탐색
최단경로 탐색에 유리한 BFS로 풀고
방문처리 및 최단경로 표시를 dp를 이용해 표시
'''

from typing import List
from collections import deque

def solution(board:List[List[int]]) -> int:
    N = len(board)
    
    # right, down, left, up
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    board[0][0] = 1
    answer = float('inf')
    
    # (row, col, direction, cost, board)
    q = deque([(0,0,'right',0), (0,0,'down',0)])
    
    # 0 : right, 1 : donw, 2 : left, 3 : up
    dp = [[[float('inf')] * N for i in range(N)] for j in range(4)]
    k = 0
    while q:
        x, y, drt, cost = q.popleft()
        
        for i, next_drt in enumerate(['right', 'down', 'left', 'up']):
            nx, ny = x + dx[i], y + dy[i]
            
            if (
                0 <= nx < N and # boundary
                0 <= ny < N and # boundary
                not board[nx][ny] # not wall
               ):
                
                if drt == next_drt:
                    ncost = cost + 100
                else:
                    ncost = cost + 600

                if ncost < dp[i][nx][ny]:
                    dp[i][nx][ny] = ncost
                    
                    if nx == N-1 and ny == N-1:
                        continue
                        
                    q.appendleft((nx, ny, next_drt, ncost))
        
    for i in range(4):
        answer = min([answer, dp[i][N-1][N-1]])
        
    return answer