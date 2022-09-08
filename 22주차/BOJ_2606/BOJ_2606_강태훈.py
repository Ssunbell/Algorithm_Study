from collections import deque
import sys
input = sys.stdin.readline
# 입력 받고 그래프, 방문표시, 방문노드 저장용 집합, 큐 설정
node_num = int(input())
link_num = int(input())
network = [[False] * node_num for _ in range(node_num)]
for _ in range(link_num):
    a, b = map(lambda x: x - 1, map(int, input().split()))
    network[a][b] = True
    network[b][a] = True
visited = [False] * node_num
answer = set([])
que = deque([0])
# BFS로 탐색하며 연결된 노드들을 answer에 저장
while que:
    curr_node = que.popleft()
    answer.add(curr_node)
    visited[curr_node] = True
    for next_node, linked in enumerate(network[curr_node]):
        if linked and not visited[next_node]:
            que.append(next_node)
# 연결된 노드들 중 자기 자신을 제외한 노드의 개수 출력
print(len(answer) - 1)
