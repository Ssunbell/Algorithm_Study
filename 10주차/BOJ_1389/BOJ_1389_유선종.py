import sys

input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())  
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, root):
    answer = [0] * (n + 1)
    visited = [root]
    dp = []
    dp.append(root)

    while dp:
        root = dp.pop(0)
        for node in graph[root]:
            if node not in visited:
                answer[node] = answer[root] + 1
                visited.append(node)
                dp.append(node)
                
    return sum(answer)


result = [bfs(graph, i) for i in range(1, n+1)]
print(result.index(min(result))+1)