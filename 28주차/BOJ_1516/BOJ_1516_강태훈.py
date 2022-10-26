import heapq
import sys
input = sys.stdin.readline


def solution(n):
    answer = [0 for _ in range(n)]
    node_w, graph = [], [[] for _ in range(n)]
    around = [0 for _ in range(n)]
    for idx in range(n):
        info = list(map(int, input().split()))[:-1]
        node_w.append(info[0])
        nodes = info[1:]
        around[idx] += len(nodes)
        for k in info[1:]:
            graph[k-1].append(idx)
    h = [(node_w[i], i) for i in range(n) if not around[i]]
    while h:
        t, build = heapq.heappop(h)
        answer[build] = t
        for p in graph[build]:
            around[p] -= 1
            if not around[p]:
                heapq.heappush(h, (t + node_w[p], p))
    print(*answer, sep='\n')


if __name__ == "__main__":
    solution(n=int(input()))
