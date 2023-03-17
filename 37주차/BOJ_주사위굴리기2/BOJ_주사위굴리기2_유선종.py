import sys
from typing import *
from collections import deque

input = lambda: sys.stdin.readline().strip()

def dice_move(d:List[int], direction:int) -> List[int]:
    if direction == 0: # up
        return [d[4], d[0], d[2], d[3], d[5], d[1]]
    elif direction == 1: # right
        return [d[2], d[1], d[5], d[0], d[4], d[3]]
    elif direction == 2: # down
        return [d[1], d[5], d[2], d[3], d[0], d[4]]
    elif direction == 3: # left
        return [d[3], d[1], d[0], d[5], d[4], d[2]]
        
def dice_rotate(dice:List[int], value:int, direction:int) -> Tuple[List[int], int]:
    dice = dice_move(dice, direction)
    if dice[0] > value:
        direction = (direction + 1) % 4
    elif dice[0] < value:
        direction = (direction - 1) % 4
    
    return dice, direction

N, M, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
total = 0
# [아래, 앞, 오른, 왼, 뒤, 위]
dice = [6, 5, 3, 4, 2, 1]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = 1
q = deque([])
q.append((0,0))
while K:
    x, y = q.popleft()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx<0 or nx>=N or ny<0 or ny>=M:
        direction = (direction - 2) % 4
        nx = x + dx[direction]
        ny = y + dy[direction]
    dice, direction = dice_rotate(dice, array[nx][ny], direction)
    q.append((nx, ny))
    q2 = deque([])
    q2.append((nx, ny))
    visited = [[False] * M for _ in range(N)]
    visited[nx][ny] = True
    b = array[nx][ny]
    c = 1
    while q2:
        nx, ny = q2.popleft()
        for i in range(4):
            nnx = nx + dx[i]
            nny = ny + dy[i]
            if 0<=nnx<N and 0<=nny<M:
                if not visited[nnx][nny] and array[nx][ny] == array[nnx][nny]:
                    visited[nnx][nny] = True
                    q2.append((nnx, nny))
                    c += 1
    total += b * c
    K -= 1 
print(total)