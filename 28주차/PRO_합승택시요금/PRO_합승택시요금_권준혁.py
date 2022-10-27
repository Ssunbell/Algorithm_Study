import heapq as hq
def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for c,d,f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    INF = 100000 * 200 + 1
    dis = [[INF] * (n + 1) for _ in range(n + 1)]
    # 모든 정점에 대해 다른 정점으로 가는 최단 거리 구하기
    for start in range(1, n + 1):
        q = []
        # (시작정점, 비용)
        hq.heappush(q, (start, 0))
        while(q):
            now, cost = hq.heappop(q)
            # now 정점에 대해서 처리한 적이 있고, 최단 경로보다 큰 경우 pass
            if dis[start][now] <= cost:
                continue
            dis[start][now] = cost
            for next_n, next_c in graph[now]:
                c = next_c + cost
                if c >= dis[start][next_n]:
                    continue
                hq.heappush(q, (next_n, c))
    answer = 2 * INF
    for sep in range(1, n + 1):
        c = dis[s][sep] + dis[sep][a] + dis[sep][b]
        answer = min(answer, c)
    return answer