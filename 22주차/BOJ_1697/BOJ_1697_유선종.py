from collections import deque

N, K = map(int, input().split())

visited = [0] * 100001
def bfs():
    q = deque()
    q.append(N)
    visited[N] += 1
    while q:
        node = q.popleft()
        will_visit = [node+1, node-1, node*2]
        for n in will_visit:
            if 0 <= n <= 100000:
                if not visited[n]:
                    visited[n] += visited[node] + 1
                    q.append(n)

bfs()
print(visited[K]-1)