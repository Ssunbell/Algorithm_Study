import sys
from collections import deque

input_s = lambda : sys.stdin.readline().strip()

n = int(input_s())
root, dest = map(int,input_s().split())
edge = int(input_s())
input_node = [list(map(int,input_s().split())) for _ in range(edge)]
graph = [[] for _ in range(n+1)]

for node in input_node:
    first = node[0]
    second = node[1]
    graph[first].append(node[1])
    graph[second].append(node[0])

def dfs(graph,root,dest):
    stack_s = deque()
    stack_s.append(root)
    visited = deque()
    depth = 0
    depth_chart = [-1]*(len(graph))
    depth_chart[root] = 0
    while stack_s:
        curr = stack_s.pop()
        visited.append(curr)
        if depth_chart[curr] == -1:
            depth += 1
        elif curr == root:
            depth = 0
        else:
            depth = depth_chart[curr]
        for node in graph[curr]:
            if node not in visited and node not in stack_s:
                stack_s.append(node)
                depth_chart[node] = depth + 1
    result = depth_chart[dest]
    return result

print(dfs(graph,root,dest))
        