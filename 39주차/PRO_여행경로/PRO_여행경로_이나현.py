#프로그래머스 여행경로
# 일반적인 dfs 문제처럼 트리형태의 계층적인 구조가 아니라 연속되는 형태의 구조
# 한번 쓴 티켓은 다시 못쓰기 때문에 재귀로 타고갈때마다 그래프구조가 독립적이어야함 -> deepcopy

from collections import defaultdict
from copy import deepcopy

def dfs(dep, graph, cnt, l):
    global answer
    if dep not in graph or len(graph[dep]) == 0:
        return
    for des in graph[dep]:
        answer += [des]
        next_graph = deepcopy(graph)
        next_graph[dep].remove(des)
        dfs(des, next_graph, cnt+1, l)
        if len(answer) == l+1:
            return
        answer.pop()


def solution(tickets):
    global answer
    graph = defaultdict(lambda:[])
    for dep, des in tickets:
        graph[dep].append(des)
    graph = {key: sorted(graph[key]) for key in graph}
    answer = ["ICN"]
    dfs("ICN", graph, 0, len(tickets))
    return answer


print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))
# print(solution([["ICN","ATL"],["ICN","ATL"],["ATL","ICN"]]))
print(solution([["ICN","ATL"],["ICN","SFO"],["SFO","ICN"]]), ["ICN","SFO","ICN","ATL"])
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]), ["ICN", "JFK", "HND", "IAD"])
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]), ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])