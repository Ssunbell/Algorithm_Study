import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def check(N, board):
    for x in range(N):
        if 0 in board[x]:
            return False
    return True

def solution(N, M, board):
    virus = []
    for x in range(N):
        for y in range(N):
            if board[x][y] == 2:
                virus.append([x, y])
    total_min_time = -float("inf")

    for selected_virus in combinations(virus, M):
        virus_on = set(map(tuple, selected_virus))
        que = deque()
        for v in virus_on:
            que.append(v)
        tmp_board = [[] for _ in range(N)]
        for x in range(N):
            tmp_board[x] = board[x][:]

        k = 0
        while que:
            k -= 1
            for _ in range(len(que)):
                x, y = que.popleft()
                for p_x, p_y in move:
                    nx, ny = x + p_x, y + p_y

                    if 0 <= nx < N and 0 <= ny < N:
                        if tmp_board[nx][ny] == 0:
                            tmp_board[nx][ny] = k
                            que.append([nx, ny])

                        elif tmp_board[nx][ny] == 2:
                            if (nx, ny) not in virus_on:
                                virus_on.add((nx, ny))
                                que.append([nx, ny])
        if not check(N, tmp_board):
            continue
        this_min_time = 0
        for x in range(N):
            for y in range(N):
                if this_min_time > tmp_board[x][y]:
                    this_min_time = tmp_board[x][y]
        total_min_time = max(total_min_time, this_min_time)
    print(-total_min_time if total_min_time != -float("inf") else -1)

if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(N, M, [list(map(int, input().split())) for _ in range(N)])