#[파괴되지 않은 건물]
def solution(board, skill):
    N = len(board)
    M = len(board[0])
    filter = [[0]*(M+1) for _ in range(N+1)]
    for s in skill:
        type, r1, c1, r2, c2, degree = s
        if type == 1:
            filter[r1][c1] -= degree
            filter[r1][c2+1] += degree
            filter[r2+1][c1] += degree
            filter[r2+1][c2+1] -= degree
        else:
            filter[r1][c1] += degree
            filter[r1][c2+1] -= degree
            filter[r2+1][c1] -= degree
            filter[r2+1][c2+1] += degree
    for i in range(1, N):
        filter[i][0] += filter[i-1][0]
    for j in range(1, M):
        filter[0][j] += filter[0][j-1]
    for i in range(1, N):
        for j in range(1, M):
            filter[i][j] += filter[i-1][j] + filter[i][j-1] - filter[i-1][j-1]
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] + filter[i][j] > 0:
                answer += 1
    return answer

print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))


# for i in range(N):
#         for j in range(M):
#             board[i][j] += filter[i][j]
#             board[i][j] = max(0, board[i][j])
#     one_d_board = sum(board, [])
#     answer = N * M - one_d_board.count(0)
#     return answer