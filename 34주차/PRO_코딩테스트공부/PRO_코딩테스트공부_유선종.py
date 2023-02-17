from heapq import heappop, heappush
from collections import deque
from typing import *

def solution(alp:int, cop:int, problems:List[int]):
    problems = deque(problems)
    problems.appendleft([0, 0, 1, 0, 1]) # only alp
    problems.appendleft([0, 0, 0, 1, 1]) # only cop

    alp_max = 0
    cop_max = 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        alp_max = max(alp_max, alp_req)
        cop_max = max(cop_max, cop_req)
    
    dp = {(alp, cop): 0}
    hq = [(0, (alp, cop))]
    while (
        hq[0][1][0] < alp_max or
        hq[0][1][1] < cop_max
    ):
        current_cost, (current_alp, current_cop) = heappop(hq)
        
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if (
                current_alp >= alp_req and
                current_cop >= cop_req
            ): # 풀어야할 문제를 정의
                total_cost = current_cost + cost
                
                # 문제의 조건보다 더 큰 경우가 발생 -> min으로 boundary 설정
                state = (min(current_alp+alp_rwd,150), min(current_cop+cop_rwd,150))
                
                if (
                    state not in dp or
                    total_cost < dp[state]
                ): # dp에 없거나 dp보다 낮은 값일 경우
                    dp[state] = total_cost
                    heappush(hq, (total_cost, state))
                
    return hq[0][0]

if __name__=='__main__':
    print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))
    print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))