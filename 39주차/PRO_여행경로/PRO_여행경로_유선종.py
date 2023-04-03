from typing import *

def solution(tickets:List[List[str]]):
    answer = []
    airports:Dict[str, List[str]] = {}
    for depart, arrive in sorted(tickets):
        if depart in airports:
            airports[depart].append(arrive)
        else:
            airports[depart] = [arrive]
    for key in airports:
        airports[key].sort(reverse=True)
        
    stack = ["ICN"]
    while stack:
        start = stack[-1]
        try:
            stack.append(airports[start].pop())
        except:
            answer.append(stack.pop())
            
    return answer[::-1]