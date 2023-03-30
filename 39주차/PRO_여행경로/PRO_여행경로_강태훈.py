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


"""
1. 인접리스트 생성. 단, 국가순 정렬을 위해 heappush 해줌
2. ICN부터 시작하여 백트래킹, stack에 "ICN" 넣고 while문 시작
3. 스택이 빌 때 까지 반복
    3-1. 스택 최상단 원소에서 사용할 수 있는 다른 티켓이 없다면 answer에 해당 국가를 append
    3-2. 반대의 경우 스택 최상단의 국가에서 갈 수 있는 이름이 가장 빠른 국가를 stack에 삽입
4. 루프가 끝나면 answer 뒤집어서 반환
"""
