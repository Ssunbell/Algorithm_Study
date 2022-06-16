import sys

input = lambda: sys.stdin.readline().rstrip()

m, n = map(int, input().split())

# x: 세로
# y: 가로

# 동 북 서 남
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

lst = [list(input().split()) for _ in range(n)]

direction = 0 # 동:0, 북:1, 서:2, 남:3
x, y = 0, 0 # 현재 위치 값

for action in lst:

    if action[0] == 'TURN' and action[1] == '0': # 왼쪽으로 90도 회전
        direction = (direction + 1) % 4

    elif action[0] == 'TURN' and action[1] == '1': # 오른쪽으로 90도 회전
        direction = (direction - 1) % 4

    elif action[0] == 'MOVE':
        if direction == 0 or direction == 2:
            x += (dx[direction] * int(action[1]))
        elif direction == 1 or direction == 3:
            y += (dy[direction] * int(action[1]))

if x < 0 or y < 0 or x > m or y > m:
    print(-1)
else:
    print(x, y) 
