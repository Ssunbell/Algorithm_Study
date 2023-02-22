import sys
input = sys.stdin.readline

def get_sand(x, y, infos):
    global answer, board
    
    if y < 0: # (0, 0)에 도달한 상황
        return
    
    total = 0
    for dx, dy, r in infos:
        xx = x + dx
        yy = y + dy
        if r == 0: # 알파에 해당하는 부분(infos의 마지막 원소)
            sand = board[x][y] - total
        else:
            sand = int(board[x][y] * r)
            total += sand
        if 0<=xx<n and 0<=yy<n:
            board[xx][yy] += sand
        else:
            answer += sand

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ratio = [
    (1, 1, 0.01), 
    (-1, 1, 0.01), 
    (1, 0, 0.07), 
    (-1, 0, 0.07), 
    (1, -1, 0.1),
    (-1, -1, 0.1), 
    (2, 0, 0.02), 
    (-2, 0, 0.02), 
    (0, -2, 0.05), 
    (0, -1, 0.00), # 알파의 위치
]

# (1, 2) -> (-1, 2)
# (1, 2) -> (-1, -2)
# (1, 2) -> (2, -1)

info = {
    0:ratio, # left
    1:[(-y, x, z) for x,y,z in ratio], # down
    2:[(x, -y, z) for x,y,z in ratio], # right
    3:[(y, x, z) for x,y,z in ratio], # up
}

s_x, s_y = n // 2, n // 2
answer = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

repeat = 0

for i in range(2 * n - 1):
    d = i % 4
    if d == 0 or d == 2: # 왼쪽 이동, 위 이동: 토네이도 이동 고정적으로 1번 더 해야함
        repeat += 1
    for _ in range(repeat):
        next_x = s_x + dx[d]
        next_y = s_y + dy[d]
        get_sand(next_x, next_y, info[d])
        s_x, s_y = next_x, next_y

print(answer)