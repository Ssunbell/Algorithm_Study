import sys
import heapq
input = sys.stdin.readline

n = int(input())
field = [input() for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def get_near(location):
    x, y = location
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            yield nx, ny


visited = [[False]*n for _ in range(n)]


q = []
q.append([0, (0, 0)])
visited[0][0] = True
while q[0][1] != (n-1, n-1):
    cnt, location = heapq.heappop(q)
    for nx, ny in get_near(location):
        if visited[ny][nx]:
            continue
        if field[ny][nx] == "1":
            heapq.heappush(q, [cnt, (nx, ny)])
            visited[ny][nx] = True
        else:
            heapq.heappush(q, [cnt+1, (nx, ny)])
            visited[ny][nx] = True
print(q[0][0])
