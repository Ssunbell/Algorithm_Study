import sys

input = lambda : sys.stdin.readline().strip()

c = int(input())
n = int(input())

graph = [[] for _ in range(c+1)]
visited = [True for _ in range(c+1)]
for _ in range(n):
    root, node = map(int, input().split())
    graph[root].append(node)
    graph[node].append(root)

answer = []
def dfs(root):
    for node in graph[root]:
        if visited[node]:
            answer.append(node)
            visited[node] = False
            dfs(node)
dfs(1)
print(len(answer)-1)