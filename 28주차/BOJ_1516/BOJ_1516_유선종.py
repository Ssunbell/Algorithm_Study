import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n = int(input())
indegree = [0] * (n+1)
build = [[] for _ in range(n+1)]
time = [0] * (n+1)
for idx in range(n):
    edge = list(map(int, input().split()))[:-1]
    time[idx+1] = edge[0]
    for e in edge[1:]:
        build[e].append(idx+1)
        indegree[idx+1] += 1

def topology_sort():
    result = [0] * (n+1)
    q = deque()
    
    # 초기 노드 번호를 넣어주기
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        current = q.popleft()
        # dp방식으로 미리 지어야 하는 건물들의 시간도 포함
        result[current] += time[current]
    
        for i in build[current]:
            indegree[i] -= 1
            result[i] = max(result[i], result[current])
            
            if indegree[i] == 0:
                q.append(i)
    
    return result

for i in topology_sort()[1:]:
    print(i)
