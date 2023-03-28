from collections import defaultdict

def solution(tickets):
    answer = []
    airports = defaultdict(list)
    tickets.sort(key = lambda x:(x[1], x[0]))
    for depart, arrive in tickets:
        airports[depart].append(arrive)
    for key in airports:
        airports[key].sort(reverse=True)
        
    stack = ["ICN"]
    while stack:
        start = stack[-1]
        if not airports[start]:
            answer.append(stack.pop())
        else:
            stack.append(airports[start].pop())
            
    return answer[::-1]