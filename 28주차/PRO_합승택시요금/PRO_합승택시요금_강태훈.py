from itertools import product
inf = 10e9


def solution(n, s, a, b, fares):
    graph = [[inf if i != j else 0 for i in range(n)] for j in range(n)]
    for f, t, w in fares:
        graph[f-1][t-1] = graph[t-1][f-1] = w
    for k, j, i in product(range(n), repeat=3):
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return min([graph[s-1][i]+graph[i][a-1]+graph[i][b-1] for i in range(n)])
