import sys
input = sys.stdin.readline

from collections import deque

dice = [1,2,3,4,5,6]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solve(n, m, k, board):
    x, y, ans, dir = 0, 0, 0, 0
    for _ in range(k):
        if not 0<=x+dx[dir]<n or not 0<=y+dy[dir] < m:
            dir = (dir+2)%4
        x, y = x+dx[dir], y+dy[dir]
        q = deque()
        c = [[0]*m for _ in range(n)]
        
        c[x][y] = 1
        q.append([x, y])
        cnt = 0
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if c[nx][ny] == 0 and board[nx][ny] == board[x][y]:
                        cnt += 1
                        c[nx][ny] = 1
                        q.append([nx, ny])

        ans += (cnt + 1) * board[x][y]
        if dir == 0: dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif dir == 1: dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        elif dir == 2: dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif dir == 3: dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        if dice[5] > board[x][y]:
            dir = (dir+1)%4
        elif dice[5] > board[x][y]:
            dir = (dir+3)%4
    return ans

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    board = [[*map(int, input().split())] for _ in range(n)]
    print(solve(n, m, k, board))