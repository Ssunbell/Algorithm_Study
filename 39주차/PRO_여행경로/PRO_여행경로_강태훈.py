from collections import defaultdict
from heapq import heappush, heappop

def solution(tickets):
    routes = defaultdict(list)
    for a,b in tickets:
        heappush(routes[a], b)
    stack, answer = ["ICN"], []
    while stack:
        if len(routes[stack[-1]])==0:
            answer.append(stack.pop())
        else:
            stack.append(heappop(routes[stack[-1]]))
    return answer[::-1]
