# dfs 풀이
import sys
sys.setrecursionlimit(5000)

def solution(n, m, x, y, r, c, k):

    def dfs(cx, cy, cnt, string):
        if cx == r and cy == c and cnt == k:
            return string
        
        for i in range(4):
            dx, dy, d = direction[i]
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                if abs(nx-r) + abs(ny-c) <= k-cnt: #r,c에 도착할 수 있는 경우에만
                    return dfs(nx, ny, cnt+1, string+d)


    shortest_distance = abs(x-r) + abs(y-c)
    if abs(shortest_distance - k) % 2 == 1:
        return 'impossible'
    if shortest_distance > k:
        return 'impossible'
    
    cx, cy = x-1, y-1
    r, c = r-1, c-1
    cnt = 0
    direction = [(1,0,'d'),(0,-1,'l'),(0,1,'r'),(-1,0,'u')] #(i,j,명령어])
    result = dfs(cx, cy, cnt, '')
    return result

## bfs 풀이 -> 시간초과
from collections import deque
def solution(n, m, x, y, r, c, k):
    
    shortest_distance = abs(x-r) + abs(y-c)
    if abs(shortest_distance - k) % 2 == 1:
        return 'impossible'

    cx, cy = x-1, y-1
    r, c = r-1, c-1
    cnt = 0
    direction = [(1,0,'d'),(0,-1,'l'),(0,1,'r'),(-1,0,'u')]
    q = deque([[cx, cy, cnt, '']])
    while True:
        cx, cy, cnt, string = q.popleft()
        if cx == r and cy == c and cnt == k:
            answer = string
            break

        for i in range(4):
            dx, dy, d = direction[i]
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                if abs(nx-r) + abs(ny-c) <= k-cnt+1: #r,c에 도착할 수 있는 경우에만
                    q.append([nx, ny, cnt+1, string+d])
    return answer

print(solution(	2,2,1,1,1,1,4))
# print(solution(3, 4, 2, 3, 3, 1, 5))
# print(solution(2, 2, 1, 1, 2, 2, 2))
# print(solution(3, 3, 1, 2, 3, 3, 4))