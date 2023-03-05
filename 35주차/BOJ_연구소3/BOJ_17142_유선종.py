import sys
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10*8)

input = lambda : sys.stdin.readline().strip()
N, M = map(int, input().split())
array = deque([])
virus = []
for i in range(N):
    sub_array = []
    for j, n in enumerate(list(map(int, input().split()))):
        if n == 1:
            sub_array.append(-2) # 벽
        elif n == 2:
            sub_array.append(0) # 바이러스
            virus.append((i,j))
        else:
            sub_array.append(-1)
    array.append(sub_array)
    


q_all = deque([])
v = []
def dfs(idx=0, v=[]):
    if len(v) == M:
        q_all.append(v[:])
        return

    for i in range(idx, len(virus)):
        dfs(i+1,v+[virus[i]])

dfs()

def bfs(q, array):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    virus = set(q)
    time = 0
    while q:
        time += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0<=nx<N and 0<=ny<N:
                    if array[nx][ny] == -1: # 빈칸
                        array[nx][ny] = time
                        q.append((nx, ny))
                    elif array[nx][ny] == 0 and (nx, ny) not in virus:
                        virus.add((nx, ny))
                        q.append((nx, ny))

    result = 0
    for row in array:
        if -1 in row:
            return float('inf')
        else:
            result = max(result, max(row))
        
    return result

answer = float('inf')
while q_all:
    answer = min(answer, bfs(deque(q_all.popleft()), deepcopy(array)))

print(answer if answer != float('inf') else -1)