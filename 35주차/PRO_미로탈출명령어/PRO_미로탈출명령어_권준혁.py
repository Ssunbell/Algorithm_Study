# 풀이 시각: 19:30~
from collections import deque
dic = {0:'d', 1:'l', 2:'r', 3:'u'}
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

def check_possible(x, y, r, c, k):
    if k % 2:
        if not (abs(x-r) + abs(y-c)) % 2:
            return False
    else:
        if (abs(x-r) + abs(y-c)) % 2:
            return False
    if abs(x-r) + abs(y-c) > k:
        return False
    return True

def bfs(start:tuple, end:tuple, k:int, n, m):
    possible_paths = []
    start = tuple(list(start) + ['', 0]) # 이동 기록을 위함. (x, y, path, len(path))
    # 시간초과를 막기 위한 코드: 3차원 visited
    visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)] # 3차원 방문 확인 shape: (k, n, m)
    visited[1][n - 1][m - 1] = 1
    q = deque((start,))
    while(q):
        tmp = q.popleft()
        path = tmp[2] # 문자열로 표현된 이동 경로
        for i in range(4):
            xx = tmp[0] + dx[i]
            yy = tmp[1] + dy[i]
            next_path = path + dic[i]
            if len(next_path) <= k and 0<=xx<n and 0<=yy<m and visited[len(next_path)][xx][yy] == 0:
                visited[len(next_path)][xx][yy] = 1
                if xx == end[0] and yy == end[1] and len(next_path) == k:
                    possible_paths.append(next_path)
                    continue
                q.append((xx, yy, next_path))
    return possible_paths

def solution(n, m, x, y, r, c, k):
    if not check_possible(x, y, r, c, k):
        return "impossible"
    board = [[0] * m for _ in range(n)]
    # 미로 도달 조건:
    # 1. 시작점에서 출발해서
    # 2. 반드시 k번째 이동일 때 끝나는 점에 도착해야함.
    # 3. 가지를 많이 치지 않기 위해서는 다음 반복/재귀가 k + 1번째이면 return.
    # 4. 매 이동을 기록해야하므로, BFS의 각 원소 구성: (x, y, 문자열) 형태로 구성하기.
    answers = bfs((x - 1, y - 1), (r - 1, c - 1), k, n, m)
    return sorted(answers)[0]
"""
미로: n by m
이동: (x,y) -> (r,c) 이동
미로 탈출 조건:
1. 격자 안에서
2. (x,y) -> (r,c): 총 이동 거리 == k
    같은 격자 2번 이상 방문 가능
3. 미로 탈출 경로 == 이동 경로 -> 문자열로 표현 가능(l, r, u, d)
    문자열이 사전 순으로 가장 빠른 경로로 탈출
        다시 말해서, 경로를 다 구하고, 경로를 문자열로 표현한 것들을 다 모아서 sorting
'최단 경로'가 아니다!
브루트포스
주어진 조건으로 (x,y) -> (r,c) 도달이 불가능할 수 있음.
    (x,y) -> (r,c) 최단 거리가 짝수이면 k도 짝수여야하고
    (x,y) -> (r,c) 최단 거리가 홀수이면 k도 홀수여야함.
0 0 1
1 0 0
(1,0) (0,2) -> |1-0| + |0-2| = 3
|1-3| + |2-3| = 3   
"""