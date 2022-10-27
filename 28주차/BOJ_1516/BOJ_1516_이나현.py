#[게임개발]
from collections import deque
N = int(input())
tmp = [[]]+[list(map(int, input().split())) for _ in range(1,N+1)]
pre_build = [[]]+[tmp[i][1:-1] for i in range(1, N+1)]
build_time = {i: tmp[i][0] for i in range(1,N+1)}
total_time = [0] * (N + 1)
visited = []
que = deque()

for i in range(1, N+1):
    if len(pre_build[i]) == 0:
        que.append(i)
        visited.append(i)

while que:
    node = que.popleft()
    total_time[node] += build_time[node]
    for i in range(1, N+1):
        if i in visited:
            continue
        if node in pre_build[i]:    #먼저 지어야하는 건물에 node가 있다면
            pre_build[i].remove(node)
            total_time[i] = max(total_time[i], total_time[node])
        if len(pre_build[i]) == 0:  #pre_build를 모두 지은 경우
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