# 한 개 테스트 케이스 말고 다 통과되는데 아직 해결을 못했습니다...
# 카카오 해설 기반으로 풀었습니다. 
# # MAX = 10_000_000 이거 좀 신기해서 적용했습니다.
# 다른 분들 해설 참고해서 해결해보겠습니다.

"""
기본 아이디어:
    1. 다익스트라 활용: 가중치의 최대값을 최소로 만드는 경로 찾기
        1-1. 이런 경로가 여러 개 있을 경우 산봉우리 번호가 작은 것을 우선
    2. 출입구 -> 산봉우리 까지의 단방향 경로 하나만 찾으면 됨. 
        왜냐면, 돌아갈 때는 같은 경로로 돌아가는 것이 최단 경로이기 때문
"""
import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    # 다익스트라
    hq = [(0, gate) for gate in gates] # (현재 경로의 intensity, 현재 지점)
    MAX = 10_000_000
    min_dis = [MAX for _ in range(n + 1)]
    
    while hq:
        intensity, node = heapq.heappop(hq)
        if min_dis[node] <= intensity:
            continue
        min_dis[node] = intensity
        if node in summits: # 현재 노드가 산봉우리면 더 이상 진행하지 않음
            continue
        for nxt, nxt_w in graph[node]:
            nxt_w = max(intensity, nxt_w)
            if min_dis[nxt] <= nxt_w:
                continue
            heapq.heappush(hq, (nxt_w, nxt))
    
    answer = [0, MAX] # (산봉우리 번호, intensity 최소값)
    
    for summit in summits:
        if min_dis[summit] < answer[1]:
            answer[0], answer[1] = summit, min_dis[summit]
        elif min_dis[summit] == answer[1] and summit < answer[0]:
            answer[0] = summit
    return answer