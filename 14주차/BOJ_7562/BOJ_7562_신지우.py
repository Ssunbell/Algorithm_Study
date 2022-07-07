# 테스트 케이스
# i 한변의 길이
# 현재 나이트가 있는 칸
# 나이트가 이동하려고 하는 칸

from collections import deque
import sys
input = lambda:sys.stdin.readline().rstrip()

t = int(input())

def bfs(cx, cy, tx, ty):

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    queue = deque()
    queue.append((cx, cy))
    chess_board[cx][cy] = 1

    while queue:
        x, y = queue.popleft()
        if x == tx and y == ty:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if chess_board[nx][ny] == 0:
                chess_board[nx][ny] = chess_board[x][y] + 1
                queue.append((nx, ny))

    return chess_board[tx][ty]-1


for i in range(t):
    n = int(input())
    cx, cy = map(int, input().split())
    tx, ty = map(int, input().split())
    
    chess_board = [([0] * n) for i in range(n)]

    print(bfs(cx, cy, tx, ty))
