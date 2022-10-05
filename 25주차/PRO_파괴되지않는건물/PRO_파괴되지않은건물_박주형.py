# 못 푼 문제

def skillCheck(s_map, skill):
    for action in skill:
        r1 = action[1]; c1 = action[2]; r2 = action[3]; c2 = action[4]
        degree = action[5]
       
        if action[0] == 1: 
            s_map[r1][c1] -= degree
            s_map[r1][c2+1] += degree
            s_map[r2+1][c1] += degree
            s_map[r2+1][c2+1] -= degree
        else: 
            s_map[r1][c1] += degree
            s_map[r1][c2+1] -= degree
            s_map[r2+1][c1] -= degree
            s_map[r2+1][c2+1] += degree
   
    for r in range(n+1): 
        for c in range(1, m+1):
            s_map[r][c] += s_map[r][c-1]
           
    for c in range(m+1): 
        for r in range(1, n+1):
            s_map[r][c] += s_map[r-1][c]      
    return
           
def solution(board, skill):
    global n, m
    n = len(board); m = len(board[0])
    s_map = [[0]*(m+1) for _ in range(n+1)]
    skillCheck(s_map, skill)
   
    answer = 0
    for r in range(n):
        for c in range(m):
            if s_map[r][c] + board[r][c] > 0:
                answer += 1
               
    return answer