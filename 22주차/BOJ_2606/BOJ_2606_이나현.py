#[바이러스]

def dfs(x):
    global count
    for node in adjacent[x]:
        if visited[node] == False:
            visited[node] = True
            count += 1
            dfs(node)

N = int(input())
M = int(input())
adjacent = [[] for _ in range(N+1)]
visited = [False] * (N+1)
visited[1] = True
for m in range(M):
    a, b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)
count = 0
dfs(1)
print(count)