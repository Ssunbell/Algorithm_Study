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
                current = q.popleft()
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

'''
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
ices = set([(x, y) for x in range(m) for y in range(n) if field[y][x] != 0])
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def get_near(location: tuple) -> tuple:
    x, y = location
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            yield (nx, ny)


def do_melting_and_count_iceberg():
    global ices
    cnt = 0
    visited = defaultdict(lambda: False)
    melt = defaultdict(int)

    for current_location in ices:
        if visited[current_location]:
            continue
        q = deque()
        q.append(current_location)
        cnt += 1
        if cnt > 1:
            return False
        while q:
            curr = q.popleft()
            visited[curr] = True
            for next_loc in get_near(curr):
                if next_loc not in ices:
                    melt[curr] += 1
                elif not visited[next_loc]:
                    q.append(next_loc)
                    visited[next_loc] = True
    for (x, y), val in melt.items():
        field[y][x] = max(0, field[y][x] - val)
        if field[y][x] == 0:
            ices = ices - set([(x, y)])
    return True


answer = 0
while do_melting_and_count_iceberg():
    answer += 1
print(answer)

'''
