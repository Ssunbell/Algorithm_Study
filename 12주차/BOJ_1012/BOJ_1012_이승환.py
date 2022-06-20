import sys
from collections import deque

input_s = lambda : sys.stdin.readline().strip()

t = int(input_s())

for _ in range(t):
    m, n, k = map(int, input_s().split())

    farm = [[0]*50 for _ in range(50)]

    # 1단계 : 모든 좌표를 큐에 넣는다
    # 2단계 : farm에서 모든 좌표에 1 값을 채운다.
    # 3단계 : 전체 큐를 돌려서 각각의 좌표마다 탐색을 실시한다
    # 4단계 : 반복문을 다시 사용하여 각 큐마다 bfs를 실시한다.
    # 5단계 : 탐색이 끝나면 cnt += 1

    q = deque()
    for _ in range(k):
        i, j = map(int, input_s().split())
        q.append((i, j))  # 1단계
        farm[i][j] = 1  # 2단계 : x가 j고 y가 i이기 때문에 바꿔줘야하지만 그냥 헷갈리지 않기 위해서 그대로감

    cnt = 0
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    while q:  # 3단계
        curr = q.popleft()
        bfsq = deque()
        bfsq.append(curr)

        visited = deque()
        while bfsq:  # 4단계
            cur = bfsq.popleft()
            visited.append(cur)
            for i in range(4):
                if cur[0]+di[i] >= 0 and cur[0]+di[i] < m and cur[1]+dj[i] >= 0 and cur[1]+dj[i] < n:
                    if farm[cur[0]+di[i]][cur[1]+dj[i]] == 1 and (cur[0]+di[i],cur[1]+dj[i]) not in bfsq and (cur[0]+di[i],cur[1]+dj[i]) not in visited:
                        bfsq.append((cur[0]+di[i],cur[1]+dj[i]))
                        try:
                            q.remove((cur[0]+di[i],cur[1]+dj[i])) # 큐가 무의미하게 돌아가는것을 막는것
                        except:
                            pass
        cnt += 1

    print(cnt)