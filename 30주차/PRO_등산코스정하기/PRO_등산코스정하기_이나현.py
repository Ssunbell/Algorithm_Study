#[프로그래머스_등산코스정하기]
from collections import defaultdict
import heapq

INF = 1e8
def solution(n, paths, gates, summits):
    
    def get_answer(n):
        distance = [INF]*(n+1)
        q = []
        for gate in gates:
            heapq.heappush(q, (0, gate))
            distance[gate] = 0
        
        while q:
            dist, now = heapq.heappop(q)
            if now in summits:
                continue
            if distance[now] < dist:
                continue
            for node, d in graph[now]:
                if node in gates_set:
                    continue
                #distance[node] = 1->3
                #dist = 1->2, d = 2->3
                cost = max(dist, d)
                if distance[node] > cost:
                    distance[node] = cost
                    heapq.heappush(q, (cost, node))

        answer = [0, INF]
        for s in summits:
            if distance[s] < answer[1]:
                answer = [s, distance[s]]
            elif distance[s] == answer[1] and s < answer[0]:
                answer = [s, distance[s]]
        return answer

    graph = defaultdict(lambda:[])
    for a, b, dist in paths:
        graph[a].append((b, dist))
        graph[b].append((a, dist))
    summits.sort()
    summits = set(summits)
    gates_set = set(gates)

    answer = get_answer(n)
    return answer


'''시간 초과
def solution(n, paths, gates, summits):
    
    def get_answer(node, n):
        distance = [INF]*(n+1)
        distance[node] = 0
        q = []
        heapq.heappush(q, (0, node))

        while q:
            dist, now = heapq.heappop(q)
            if now in set(summits):
                continue
            if distance[now] < dist:
                continue
            for node, d in graph[now]:
                if node in set(gates):
                    continue
                #distance[node] = 1->3
                #dist = 1->2, d = 2->3
                cost = max(dist, d)
                if distance[node] > cost:
                    distance[node] = cost
                    heapq.heappush(q, (cost, node))
        return distance        

    graph = defaultdict(lambda:[])
    for a, b, dist in paths:
        graph[a].append((b, dist))
        graph[b].append((a, dist))
    answer = [0, INF]
    summits.sort()
    for gate in gates:
        short_list = get_answer(gate, n)
        for summit in summits:
            if short_list[summit] < answer[1]:
                answer = [summit, short_list[summit]]
    return answer
'''
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])) #[3,4]
print(solution(	7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))