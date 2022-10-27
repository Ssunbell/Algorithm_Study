from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().strip())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
cost = [0] * (n + 1)

for i in range(1, n + 1):
    info = list(map(int,input().split()[:-1]))
    cost[i] = info[0]
    if len(info) >= 2:
        for j in info[1:]:
            # 정점 j -> 정점 i로 이동 가능
            graph[j].append(i)
        indegree[i] += len(info[1:])

def topology_sort():
    q = deque()
    res = [0] * (n + 1)
    
    # 위상정렬 초기화: 진입차수가 0인 노드들 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        res[now] += cost[now]
        for i in graph[now]:
            indegree[i] -= 1
            res[i] = max(res[i], res[now])
            if indegree[i] == 0:
                q.append(i)
    return res

for i in topology_sort()[1:]:
    print(i)