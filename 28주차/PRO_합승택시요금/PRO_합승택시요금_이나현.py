#[프로그래머스_합승택시요금]
import heapq

INF = 10**9
def solution(n, s, a, b, fares): #n:노드 수, s:시작점, fares:각 간선사이의 요금이 담긴 2차원배열
    
    def dikjstra(start, n):
        q = []
        distance = [INF] * (n+1)
        distance[start] = 0
        heapq.heappush(q, (0, start))
        
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distance


    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    start_fare = dikjstra(s, n)             #start 지점에서 다른 노드들까지 가는데 필요한 최소 요금 list
    answer = start_fare[a] + start_fare[b]
    for node in range(1, n+1):
        if node == s:
            continue
        node_fares = dikjstra(node, n)      #node 지점에서 다른 노드들까지 가는데 필요한 최소 요금 list
        node_fare = node_fares[s] + node_fares[a] + node_fares[b]
        answer = min(answer, node_fare)
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))