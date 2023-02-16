import sys
from typing import *

def direction_step_list(N:int) -> List[Tuple[str, int]]:
    '''N이 홀수인 조건에 따라 토네이도 방향 및 이동하는 칸의 크기를 list에 담아줌'''
    directions = ['left', 'down', 'right', 'up']
    direction_step_list = []
    for step in range(1, N):
        for c in range(2):
            direction_step_list.append((directions[((step-1)*2)%4+c], step))
    direction_step_list.append((directions[((N-1)*2)%4], N-1))
            
    yield from direction_step_list
    
def move_points(points:List[int], direction:str) -> List[int]:
    '''방향에 따라 [row,col] 좌표를 옮겨주는 함수'''
    if direction == 'left':
        points[1] -= 1
    elif direction == 'down':
        points[0] += 1
    elif direction == 'right':
        points[1] += 1
    elif direction == 'up':
        points[0] -= 1
        
    return points

def sand_split(
    array:List[List[int]], 
    points:List[int], 
    direction:str
) -> Tuple[List[List[int]], int]:
    '''토네이도로 인해 흩뿌려진 모레를 array에 반영하고
    격자 밖으로 나간 모레를 더해주는 함수'''
    row, col = points
    N = len(array)
    y = array[row][col]
    array[row][col] = 0
    # left 기준
    t = [
        [-2, 0, int(0.02 * y)], # 2%
        [-1, -1, int(0.1 * y)], # 10%
        [-1, 0, int(0.07 * y)], # 7%
        [-1, +1, int(0.01 * y)], # 1%
        [0, -2, int(0.05 * y)], # 5%
        [+1, -1, int(0.1 * y)], # 10%
        [+1, 0, int(0.07 * y)], # 7%
        [+1, +1, int(0.01 * y)], # 1%
        [+2, 0, int(0.02 * y)], # 2%
        ]
    
    alpha = y - ((int(0.02 * y)+int(0.1 * y)+int(0.07 * y)+int(0.01 * y))*2+int(0.05 * y))
        
    if direction == 'left':
        tornado_list = [[row+g[0], col+g[1], g[2]] for g in t]
        tornado_list.append([row, col-1, alpha]) # alpha
    elif direction == 'down':
        tornado_list = [[row-g[1], col+g[0], g[2]] for g in t]
        tornado_list.append([row+1, col, alpha]) # alpha
    elif direction == 'right':
        tornado_list = [[row+g[0], col-g[1], g[2]] for g in t]
        tornado_list.append([row, col+1, alpha]) # alpha
    elif direction == 'up':
        tornado_list = [[row+g[1], col+g[0], g[2]] for g in t]
        tornado_list.append([row-1, col, alpha]) # alpha
    
    out = 0
    for tornado in tornado_list:
        r, c, ratio = tornado
        if 0<=r<N and 0<=c<N:
            array[r][c] += ratio
        else:
            out += ratio

    return (array, out)
    
if __name__=='__main__':
    input = lambda : sys.stdin.readline().strip()

    N = int(input())
    array = [list(map(int,input().split())) for _ in range(N)]
    points = [N//2,N//2]
    count = 0
    for direction, step in direction_step_list(N):
        for _ in range(1, step+1):
            points = move_points(points, direction)
            outputs = sand_split(array, points, direction)
            array = outputs[0]
            count += outputs[1]
    
    print(count)