import sys
def input(): return sys.stdin.readline().strip()


n = int(input())

for i in range(1, 3):
    if i == 1:
        o, p = map(int, input().split())
    else:
        m = int(input())

graph = [[] for _ in range(n+1)]

for j in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(o):
    for i in graph[o]:
        if visited[i] == 0:
            visited[i] = visited[o] + 1
            dfs(i)


visited = [0] * int(n+1)

dfs(o)
print(visited[p] if visited[p] > 0 else -1)
