from heapq import heappop, heappush
INF = 10000001

def solution(n, paths, gates, summits):
    graph = [[INF]*n for _ in range(n)]
    gates = list(map(lambda x:x-1, gates))
    for i,j,w in paths:
        graph[i-1][j-1] = graph[j-1][i-1] = w
    summits = list(map(lambda x:x-1, summits))
    answer = [INF, INF]

    
    pq = []
    distance = [INF]*n
    for gate in gates:
        distance[gate] = 0
        heappush(pq, (0,gate))
    while pq:
        cintensity, cnode = heappop(pq)
        if distance[cnode] < cintensity or cnode in summits:
            continue
        for nnode, nintensity in enumerate(graph[cnode]):
            big = max(cintensity, nintensity)
            if big < distance[nnode]:
                distance[nnode] = big
                heappush(pq, (big, nnode))
                
    for summit in sorted(summits, reverse=True):
        if distance[summit] <= answer[1]:
            answer = [summit+1, distance[summit]]
    return answer






tc=[[6,	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],	[1, 3],	[5],	[5, 3]],
    [7,	[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],	[1],	[2, 3, 4],	[3, 4]],
    [7,	[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],	[3, 7],	[1, 5],	[5, 1]],
    [5,	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],	[1, 2],	[5],	[5, 6]],
]
for idx, c in enumerate(tc):
    print(idx+1,"---------------------------------------")
    print(f"{solution(*c[:-1])}________{c[-1]}")
    if solution(*c[:-1])==c[-1]:
        print("Correct answer!!")
    else:
        print("Retry..")