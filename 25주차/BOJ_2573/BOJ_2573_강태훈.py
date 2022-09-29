import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ice = set([(x, y)for x in range(m) for y in range(n) if graph[y][x] > 0])
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def get_near_coordinate(location: tuple):
    x, y = location
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            yield nx, ny


def count_sea(location: tuple) -> int:
    x, y = location
    cnt = 0
    for nx, ny in get_near_coordinate(location):
        if graph[ny][nx] == 0:
            cnt += 1
    return cnt


def is_splitted():
    visited = {c: False for c in ice}
    cnt = 0
    for location in ice:
        if visited[location]:
            continue
        else:
            if cnt == 1:
                return True
            cnt += 1
            q = deque()
            q.append(location)
            while q:
                current = q.pop()
                visited[current] = True
                for next_location in get_near_coordinate(current):
                    nx, ny = next_location
                    if next_location in ice and not visited[next_location] and graph[ny][nx] > 0:
                        q.append(next_location)
    return False


year = 0
while not is_splitted():
    if not ice:
        year = 0
        break
    del_set = set()
    melt_dict = {(x, y): count_sea(location=(x, y)) for x, y in ice}
    for x, y in ice:
        graph[y][x] = max(graph[y][x] - melt_dict[(x, y)], 0)
        if graph[y][x] == 0:
            del_set.add((x, y))
    ice = ice - del_set
    year += 1
print(year)
