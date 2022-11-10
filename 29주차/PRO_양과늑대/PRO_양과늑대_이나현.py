from collections import defaultdict, deque

def solution(info, edges):
    graph = defaultdict(lambda:[])
    for a, b in edges:
        graph[a].append(b)
    
    q = deque()
    q.append([0,1,0,set()]) #현재 노드, 양의 수, 늑대의 수, 다음 탐색할 노드집합
    max_sheep = 0
    while q:
        now, sheepCount, wolfCount, nextNode = q.popleft()
        nextNode.update(graph[now])
        max_sheep = max(max_sheep, sheepCount)

        for next in nextNode:
            if info[next] == 0:
                q.append([next, sheepCount+1, wolfCount, nextNode - {next}])
            else:
                if sheepCount > wolfCount + 1:
                    q.append([next, sheepCount, wolfCount+1, nextNode - {next}])
    return max_sheep
                
print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))