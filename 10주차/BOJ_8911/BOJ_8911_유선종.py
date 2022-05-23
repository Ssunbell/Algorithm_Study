import sys

input = lambda : sys.stdin.readline().strip()
t = int(input())
commands = [list(input()) for _ in range(t)]

# 위치 커맨드
#     왼 위 오른 아래
x = [-1, 0, 1, 0] # x축
y = [0, 1, 0, -1] # y축

for command in commands:
    nx, ny = 0, 0
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    dir = 2

    for cm in command:
        if cm == 'L':
            dir = (dir - 1) % 4
        elif cm == 'R':
            dir = (dir + 1) % 4
        elif cm == 'F':
            nx += x[dir]
            ny += y[dir]
        elif cm == 'B':
            nx -= x[dir]
            ny -= y[dir]
            # nx += dx[dir+2]
            # ny += dx[dir+2]
        min_x = min(min_x, nx)
        min_y = min(min_y, ny)
        max_x = max(max_x, nx)
        max_y = max(max_y, ny)
    print(abs(max_x - min_x) * abs(max_y - min_y))