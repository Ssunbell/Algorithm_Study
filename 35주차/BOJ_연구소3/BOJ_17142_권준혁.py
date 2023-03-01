import sys
input = sys.stdin.readline
from copy import deepcopy
from collections import deque
"""
1. 2의 위치들 중 M개 선택
2. 선택한 위치에 대해 바이러스 퍼지기 시작 (매 반복을 += 1)
    종료 조건: 모든 활성 바이러스의 위치들에 대해 BFS를 진행했는데도, 전체에서 0이 남아 있으면 안됨.
3. 1~2를 모든 조합에 대해 시도해서 최소값 구함.
"""
def comb(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield [arr[i]]
        else:
            for next in comb(arr[i + 1:], k - 1):
                yield [arr[i]] + next

def BFS(board_copy, visited, active_virus_loc):
    if zero == 0:
        return 0
    cnt = 0
    cnt_zero = 0
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    q = [active_virus_loc[:]]
    for i, j in active_virus_loc:
        visited[i][j] = 1
    while(q):
        next_virus = []
        tmp = q[0]
        q = []
        for x, y in tmp:
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0<=xx<n and 0<=yy<n and visited[xx][yy] == 0 and board_copy[xx][yy] != 1 and board_copy[xx][yy] != 3:
                    if board_copy[xx][yy] == 0:
                        cnt_zero += 1
                        board_copy[xx][yy] = 3
                        if cnt_zero == zero:
                            return cnt + 1
                    next_virus.append((xx, yy))
                    visited[xx][yy] = 1
                    board_copy[xx][yy] = 3
        if not next_virus:
            break
        else:
            q.append(next_virus)
            cnt += 1
    return cnt

if __name__ == "__main__":
    answer = []
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 2의 위치 찾기
    locs = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 2]
    # 0의 개수 찾기: 종료 조건을 위함
    zero = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                zero += 1
    virus = []
    # 2의 위치 m개 선택
    for c in comb(locs, m):
        virus.append(c)
    # 2의 후보 위치에 3을 할당 (3의 의미: 활성 바이러스)
    for active_virus_loc in virus:
        board_copy = deepcopy(board)
        visited = [[0] * n for _ in range(n)]
        for i, j in active_virus_loc:
            board_copy[i][j] = 3
        # 3의 위치에서 계속 퍼지기 (방문했으면 중단)
        # 3개를 한번에 큐에 넣어서 BFS 돌려야함.
        cnt = BFS(board_copy, visited, active_virus_loc) # BFS 중단 == 바이러스가 지날 수 있는 모든 구간을 지남
        # board_copy의 모든 곳을 확인해서 0이 있는지 확인
        for i in range(n):
            ch = False
            for j in range(n):
                if board_copy[i][j] == 0:
                    answer.append(float('inf'))
                    ch = True
                    break
            if ch:
                break
        else:
            answer.append(cnt)
    mini = min(answer)
    print(-1 if mini == float('inf') else mini)