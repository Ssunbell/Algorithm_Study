from typing import *
from collections import deque

def move(i:int) -> Tuple[int, int, int, int]:
    # 동 서 남 북
    dx = (0,0,1,-1)
    dy = (1,-1,0,0)
    return dx[i], dy[i], dx[i], dy[i]
        
def rotate(i:int, condition:Tuple[str, str]) -> Tuple[int, int, int, int, int, int, int, int]:
    state, standard = condition
    if state == 'horizontal':
        # 왼쪽을 축으로 시계, 반시계 / 오른쪽을 축으로 시계, 반시계 90도 만큼 이동
        dx1 = (0, 0, -1, 1)
        dy1 = (0, 0, 1, 1)
        dx2 = (1, -1, 0, 0)
        dy2 = (-1, -1, 0, 0)
        w_x1 = (0, 0, -1, 1)
        w_y1 = (0, 0, 0, 0)
        w_x2 = (1, -1, 0, 0)
        w_y2 = (0, 0, 0, 0)
    elif state == 'vertical':
        # 위를 축으로 시계, 반시계 / 아래를 축으로 시계, 반시계 90도 만큼 이동
        dx1 = (0, 0, 1, 1)
        dy1 = (0, 0, 1, -1)
        dx2 = (-1, -1, 0, 0)
        dy2 = (-1, 1, 0, 0)
        w_x1 = (0, 0, 0, 0)
        w_y1 = (0, 0, 1, -1)
        w_x2 = (0, 0, 0, 0)
        w_y2 = (-1, 1, 0, 0)
        
    if standard == 'leftup':
        return dx1[i], dy1[i], dx2[i], dy2[i], w_x1[i], w_y1[i], w_x2[i], w_y2[i]
    elif standard == 'rightdown':
        return dx2[i], dy2[i], dx1[i], dy1[i], w_x2[i], w_y2[i], w_x1[i], w_y1[i]
        

def solution(board):
    answer = 0
    def bfs(array):
        N = len(array)
        array = [[1] + a + [1] for a in array]
        array = [[1] * (N+2)] + array + [[1] * (N+1)]
        visited = set([(1,1,1,2)])
        q = deque([(1,1,1,2,0)])

        while q:
            x1, y1, x2, y2, count = q.popleft()
            for i in range(4):
                dx1, dy1, dx2, dy2 = move(i)
                nx1 = x1 + dx1
                ny1 = y1 + dy1
                nx2 = x2 + dx2
                ny2 = y2 + dy2
                
                if array[nx1][ny1] == 0 and array[nx2][ny2] == 0:  # 벽이 없는 경우
                    if nx1 == ny1 == N or nx2 == ny2 == N:
                        return count + 1
                    
                    if (nx1, ny1, nx2, ny2) not in visited:
                        visited.add((nx1,ny1,nx2,ny2))
                        q.append((nx1, ny1, nx2, ny2, count+1))
                        
            state = 'horizontal' if (x1 - x2) == 0 else 'vertical'
            standard = 'leftup' if (x1 + y1) < (x2 + y2) else 'rightdown'
            condition = (state, standard)
            for k in range(4):
                rx1, ry1, rx2, ry2, w_x1, w_y1, w_x2, w_y2 = rotate(k, condition)
                wx1 = x1 + w_x1
                wy1 = y1 + w_y1
                wx2 = x2 + w_x2
                wy2 = y2 + w_y2
                if array[wx1][wy1] == 0 and array[wx2][wy2] == 0:
                    # 회전 이동 경로에 벽이 없다면
                    nx1 = x1 + rx1
                    ny1 = y1 + ry1
                    nx2 = x2 + rx2
                    ny2 = y2 + ry2
                    
                    if array[nx1][ny1] == 0 and array[nx2][ny2] == 0:
                        if nx1 == ny1 == N or nx2 == ny2 == N:
                            return count + 1
                        
                        if (nx1, ny1, nx2, ny2) not in visited:
                            visited.add((nx1,ny1,nx2,ny2))
                            q.append((nx1, ny1, nx2, ny2, count+1))                    
    
    return bfs(board)