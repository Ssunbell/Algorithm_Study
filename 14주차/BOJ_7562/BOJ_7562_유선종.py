import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()

t = int(input())
cases = []
for _ in range(t):
    l = int(input())
    cur_pos = list(map(int, input().split()))
    tar_pos = list(map(int, input().split()))
    cases.append([l, cur_pos, tar_pos])

    #시계방향 1 2 3 4 5 6 7 8
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

for case in cases:
    l = case[0]
    result = [[0] * l for _ in range(l)]
    cur_pos = case[1]
    tar_pos = case[2]
    s = deque()
    s.append(cur_pos)
    while s:
        pos = s.popleft()
        a, b = pos[0], pos[1]
        if a == tar_pos[0] and b == tar_pos[1]:
            print(result[a][b])
            break

        for i in range(8):
            x = a + dx[i] # x = x + dx 라고 하면 안됨
            y = b + dy[i]
            if 0 <= x < l and 0 <= y < l and result[x][y] == 0: # 메모리 방지  
                s.append([x,y])
                result[x][y] = result[a][b] + 1