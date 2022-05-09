import sys

input_s = lambda : sys.stdin.readline().strip()
n,m,v = map(int,input().split())
node = [list(map(int, input_s().split())) for _ in range(m)]

# 노드를 딕셔너리에 정리해서 문제 풀어야함.
def dfs(nodes,v):
    nodes.sort(reverse=True)
    q = []
    visited = []
    q.append(v)
    while q:    
        curr = q.pop()
        visited.append(curr)
        for edge in nodes:
            if curr == edge[0] and edge[1] not in q and edge[1] not in visited:
                q.append(edge[1])
    return visited
        
def bfs(nodes,v):
    node.sort()
    q = []
    visited = []
    q.append(v)
    while q:
        curr = q.pop(0)
        visited.append(curr)
        for edge in nodes:
            if curr == edge[0] and edge[1] not in q and edge[1] not in visited:
                q.append(edge[1])
    return visited

d = dfs(node,v)
b = bfs(node,v)
print(d)
print(b)
# for i in d:
#     print(i,end=" ")
# print()
# for i in b:
#     print(i, end=" ")

