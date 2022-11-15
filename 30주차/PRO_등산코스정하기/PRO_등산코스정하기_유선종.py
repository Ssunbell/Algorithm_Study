from heapq import heappop, heappush

def make_graph(n, fares):
    graph = [[] for _ in range(n+1)]
    for node1, node2, dist in fares:
        graph[node1].append([dist, node2])
        graph[node2].append([dist, node1])
                
    return graph

def dijkstra(graph, gates:list, summits:set):
    dp = [10000001] * (len(graph)+1)
    q = []
    for start in gates:
        dp[start] = 0
        heappush(q, [0, start])
        
    while q:
        intensity, curr = heappop(q)
            
        if curr in summits or intensity > dp[curr]:
            continue
            
        for node in graph[curr]: 
            dist, ncurr = node[0], node[1]

            # 가중치를 큰 값으로 업데이트
            next_intensity = max(dist, intensity)
            if next_intensity < dp[ncurr]: # 만약 저장된 값보다 작으면
                # 그 가중치로 발자취를 남김
                dp[ncurr] = next_intensity
                heappush(q, [next_intensity, ncurr])
                
    min_intensity = [0, 10000001]
    for summit in summits:
        if dp[summit] < min_intensity[1]:
            min_intensity[0] = summit
            min_intensity[1] = dp[summit]
        elif dp[summit] == min_intensity[1] and summit < min_intensity[0]:
            min_intensity[0] = summit

    return min_intensity

def solution(n, paths, gates, summits):
    graph = make_graph(n, paths)
    answer = dijkstra(graph, gates, set(sorted(summits)))
            
    return answer