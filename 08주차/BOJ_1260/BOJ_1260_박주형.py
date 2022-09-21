import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


n, m, v = map(int, input().split())

graph = [[] for _ in range(m)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False] * int(n+1)


print(dfs(graph, v, visited))
print(bfs(graph, v, visited))


# 계속 none 값이 나옴
