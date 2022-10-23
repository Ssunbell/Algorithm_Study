from heapq import heappop, heappush

def make_graph(n, fares):
    graph = [[] for _ in range(n+1)]
    for node1, node2, dist in fares:
        graph[node1].append([dist, node2])
        graph[node2].append([dist, node1])
                
    return graph

def dijkstra(graph, start:int, end:int):
    dp = [1e8] * (len(graph)+1)
    dp[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        dist, curr = heappop(q)
        
        if dp[curr] < dist:
            continue
            
        for node in graph[curr]: 
            ndist, ncurr = node[0], node[1]
            ndist += dist

            if ndist < dp[ncurr]:
                dp[ncurr] = ndist
                heappush(q, [ndist, ncurr])
                
    return dp[end]
    
def solution(n, s, a, b, fares):
    graph = make_graph(n, fares)
    dist_min = dijkstra(graph, s, a) + dijkstra(graph, s, b)
    for i in range(1, n+1):
        if s!= i:
            dist_min = min(dist_min, dijkstra(graph, s, i) + dijkstra(graph, i, a) + dijkstra(graph, i,b))
            
    return dist_min