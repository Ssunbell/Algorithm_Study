#[게임개발]
from collections import deque
N = int(input())
tmp = [[]]+[list(map(int, input().split())) for _ in range(1,N+1)]
pre_build = [[]]+[tmp[i][1:-1] for i in range(1, N+1)]
build_time = {i: tmp[i][0] for i in range(1,N+1)}
total_time = [0] * (N + 1)
visited = []
que = deque()

# 1.진입차수가 0인 정점을 큐에 추가
for i in range(1, N+1):
    if len(pre_build[i]) == 0:
        que.append(i)
        visited.append(i)

while que:
    node = que.popleft()
    total_time[node] += build_time[node]
    # 2.큐에서 꺼낸 원소에 연결된 모든 간선을 제거
    for i in range(1, N+1):
        if i in visited:
            continue
        if node in pre_build[i]:
            pre_build[i].remove(node)
            total_time[i] = max(total_time[i], total_time[node])
        # 3.간선 제거 이후 진입차수가 0인 정점을 큐에 추가
        if len(pre_build[i]) == 0:
            que.append(i)
            visited.append(i)
print(*total_time[1:], sep='\n')

'''
5
10 -1
20 1 -1
30 2 -1
40 3 5 -1
100 -1

실제 정답 :
10
30
60
140
100
'''