# 첫 줄에 대한 모든 경우의 수에 대하여 완전탐색 하지만, 이후엔 그리디로 접근한다.

from itertools import product
from copy import deepcopy
near = [(0,1),(0,-1),(1,0),(-1,0),(0,0)]

def get_near(board, loc):
    n = len(board)
    x, y = loc
    for dx, dy in near:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n:
            yield (nx,ny)

action = lambda x, val: (x+val)%4

def turn(board, loc, val):
    for nx, ny in get_near(board, loc):
        board[ny][nx] = action(board[ny][nx], val)
    return board

def process_line(graph, case, line):
    for idx, val in enumerate(case):
        if not val:
            continue
        turn(graph, (idx, line), val)
    
def solution(clockHands):
    answer = float("inf")
    n = len(clockHands)
    for case in product(range(4), repeat=n):
        graph = deepcopy(clockHands)
        cnt = sum(case)
        process_line(graph, case, 0)
        for i in range(1, n):
            new_case = [(4-i)%4 for i in graph[i-1]]
            process_line(graph, new_case, i)
            cnt += sum(new_case)
        if sum(graph[-1]) == 0:
            answer = min(answer, cnt)
    return answer

# Try 1 : 시간초과
# 모든 줄에 대하여 완전탐색 진행
# 불필요한 연산의 중복으로 인한 시간초과로 예상됨.
"""
from itertools import combinations_with_replacement as cwr

near = [(0,1),(0,-1),(1,0),(-1,0),(0,0)]

def get_near(board, loc):
    n = len(board)
    x, y = loc
    for dx, dy in near:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n:
            yield (nx,ny)

action = lambda x: (x+1)%4

def turn(board, loc):
    tmp_board = [[dot for dot in line] for line in board]
    for nx, ny in get_near(board, loc):
        tmp_board[ny][nx] = action(tmp_board[ny][nx])
    return tmp_board

def simulatioin(board, locs):
    if not locs:
        for line in board:
            for dot in line:
                if dot != 0:
                    return False
        return True
    else:
        cmd = locs.pop()
        return simulatioin(turn(board, cmd), locs)

def solution(clockHands):
    n = len(clockHands)
    coords = [(x,y) for x in range(n) for y in range(n)]
    answer = 0
    while answer <= 256:
        for i in cwr(coords, answer):
            if simulatioin(clockHands, list(i)):
                return answer
        answer += 1
"""

if __name__ == "__main__":
    print(solution(
        [[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]]	
    ))