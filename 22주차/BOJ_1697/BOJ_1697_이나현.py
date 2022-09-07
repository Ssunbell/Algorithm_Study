#[숨바꼭질]
from collections import deque
N, K = map(int, input().split())
if N == K:
    print(0)
else:
    visited = [0] * 100001
    que = deque([N])
    while que:
        num = que.popleft()
        arr = [num-1, num+1, 2*num]
        if K in arr:
            print(visited[num] + 1)
            break
        for x in arr:
            if 0 <= x <= 100000 and visited[x] == 0:
                visited[x] = visited[num] + 1
                que.append(x)