#백준 2252 줄세우기
#위상 정렬
from collections import defaultdict, deque

N, M = map(int, input().split())
in_graph = defaultdict(list)
out_graph = defaultdict(list)
for _ in range(M):
    s, e = map(int, input().split())
    in_graph[e].append(s)
    out_graph[s].append(e)

q = deque()
for node in range(1, N+1):
    if len(in_graph[node]) == 0:
        q.append(node)

result = []
while q:
    node1 = q.popleft()
    result.append(node1)
    for node2 in out_graph[node1]:
        in_graph[node2].remove(node1)
        if len(in_graph[node2]) == 0:
            q.append(node2)

print(*result)