from ast import Lambda
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

n,m = int(input()), int(input())
graph = [[float('inf')]*n for i in range(n)]

for _ in range(m):
    s,e,w = map(int,input().split())
    s-=1
    e-=1
    graph[s][e] = min(graph[s][e], w)


for k in range(n):
    graph[k][k] = 0
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in graph:
    for j in i:
        print(j if j!=float('inf') else 0, end = " ")
    print()
    

# n = int(input())
# m = int(input())
# list_bus = [{} for _ in range(n+1)]
# for _ in range(m):
#     root, node, cost = map(int, input().split())
#     if node not in list_bus[root]:
#         list_bus[root][node] = cost
#     else:
#         if list_bus[root][node] > cost:
#             list_bus[root][node] = cost
            
# result = []
# cnt = 0
# def bfs(start, end):
#     global cnt
#     if start == end:
#         return
#     root_node = list_bus[start]

#     for node in root_node.keys():
#         cnt += root_node[node]
#         if node == end:
#             result.append(cnt)
#             return
#         bfs(node, end)
    
# bfs(4,1)
# print(cnt, result)