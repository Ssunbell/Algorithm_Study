from typing import *
from copy import deepcopy

def turn(
    clockHands:List[List[int]],
    row:int,
    col:int,
    value:int=1,
) -> List[List[int]]:
    dx = [0, 0, 0, 1, -1]
    dy = [0, 1, -1, 0, 0]
    for i in range(5):
        nx = row + dx[i]
        ny = col + dy[i]
        if 0<=nx<len(clockHands) and 0<=ny<len(clockHands[0]):
            clockHands[nx][ny] = (clockHands[nx][ny]+value)%4
    
    return clockHands

def solution(clockHands:List[List[int]]):
    answer = float('inf')
    all_cases = []
    length = len(clockHands)
    def cases(length:int, case:List[int]):
        if len(case) == length:
            all_cases.append(case)
            return

        for i in range(4):
            cases(length, case + [i])
    
    def bfs(clockHands:List[List[int]], case):
        nonlocal answer
        
        length = len(clockHands)
        cnt = 0
        for col in range(length): # 첫줄에 대한 경우의 수 실행
            count = case[col]
            if count != 0:
                clockHands = turn(clockHands, 0, col, count)
                cnt += count
        
        for row in range(1, length): # 두번째 줄부터 완전 탐색
            for col in range(length):
                if clockHands[row-1][col] == 0: continue
                
                count = 4 - clockHands[row-1][col]
                clockHands = turn(clockHands, row, col, count)
                cnt += count
                
        if all([not any(clockHands[-1])]):
            answer = min(answer, cnt)
    
    cases(length, [])
    for case in all_cases:
        bfs(deepcopy(clockHands), case)
    return answer