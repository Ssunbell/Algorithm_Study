# list를 큐 또는 덱으로 사용하면 절대, 절대, 절대, 절대, 절대 안 됩니다!! 반드시 collections.deque를 써야 합니다.
# 다음부터는 이렇게 하기!
import sys

input_s = lambda : sys.stdin.readline().strip()
n,m,v = map(int,input_s().split())
node = [list(map(int, input_s().split())) for _ in range(m)]

nodes = {}
for data in node:
    if data[0] not in nodes:
        nodes[data[0]] = [data[1]]
    elif data[0] in nodes:
        nodes[data[0]].append(data[1])
    if data[1] not in nodes:
        nodes[data[1]] = [data[0]]
    elif data[1] in nodes:
        nodes[data[1]].append(data[0])

def dfs(nodes,v):
    q = []
    visited = []
    q.append(v)
    while q:
        curr = q.pop()
        if curr not in visited:
            visited.append(curr)
            if curr in nodes:
                nodes[curr].sort(reverse = True)
                for node in nodes[curr]:
                    if node not in visited:
                        q.append(node)
    return visited
        
def bfs(nodes,v):
    q = []
    visited = []
    q.append(v)
    while q:
        curr = q.pop(0)
        visited.append(curr)
        if curr in nodes:
            nodes[curr].sort()
            for node in nodes[curr]:
                if node not in visited and node not in q:
                    q.append(node)
            
    return visited

d = dfs(nodes,v)
b = bfs(nodes,v)

for i in d:
    print(i,end=" ")
print()
for i in b:
    print(i, end=" ")

