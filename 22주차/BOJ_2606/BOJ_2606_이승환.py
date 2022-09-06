from collections import deque

num_com = int(input())
edge = int(input())

# 인덱스는 pc번호, network[i]는 i번째 컴퓨터와 연결된 pc
# 양방향 그래프이기 때문에 n1과 n2 둘다입력
network = [[] for _ in range(num_com+1)]
for i in range(1,edge+1):
    n1, n2 = map(int,input().split())
    network[n1].append(n2)
    network[n2].append(n1)

q = deque()
q.append(1)
visited = deque()
while q:
    curr = q.popleft()
    visited.append(curr)
    for node in network[curr]:
        if node not in visited and node not in q:
            q.append(node)

# 맨 처음 바이러스에 걸리는 1번pc는 제외
print(len(visited) - 1)