from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    stack = deque([])
    for i in range(1, N+1):
        if indegree[i] == 0:
            stack.append(i)

    while stack:
        cur = stack.pop()
        print(cur, end=' ')
        
        for i in graph[cur]:
            indegree[i] -= 1
            
            if indegree[i] == 0:
                stack.append(i)

topology_sort()