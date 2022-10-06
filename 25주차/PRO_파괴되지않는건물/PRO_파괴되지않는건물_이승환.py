# def solution(board, skill):
#     for stats in skill:
#         tp,i_start,j_start,i_finish,j_finish,degree = stats
        
#         if tp == 1:
#             degree = -degree
        
#         for i in range(i_start,i_finish + 1,1):
#             for j in range(j_start, j_finish + 1,1):
#                 board[i][j] += degree

#     result = sum(board,[])
#     answer = 0
#     for r in result:
#         if r > 0:
#             answer += 1
#     return answer

def solution(board, skill):
    answer = 0
    i_idx = len(board)
    j_idx = len(board[0])
    new_board = [[0]*(j_idx+1) for _ in range(i_idx+1)]
    for stats in skill:
        tp,i_start,j_start,i_finish,j_finish,degree = stats
        if tp == 1:
            degree = -degree
        new_board[i_start][j_start] += degree
        new_board[i_start][j_finish+1] -= degree
        new_board[i_finish+1][j_start] -= degree
        new_board[i_finish+1][j_finish+1] += degree
    
    for i in range(i_idx+1):
        for j in range(1,j_idx+1):
            new_board[i][j] += new_board[i][j-1]
    
    for j in range(j_idx+1):
        for i in range(1,i_idx+1):
            new_board[i][j] += new_board[i-1][j]
    
    for i in range(i_idx):
        for j in range(j_idx):
            board[i][j] += new_board[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

print(solution(board,skill))