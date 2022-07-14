
def solution(board, moves):
    answer = 0
    
    dolls = []
    
    for move in moves:
        m = move - 1

        for i in range(len(board)):
            if board[i][m] != 0:
                dolls.append(board[i][m])
                board[i][m] = 0
                if len(dolls) >= 2:
                    if dolls[-1] == dolls[-2]:
                        dolls.pop()
                        dolls.pop()
                        answer += 2
                break
    
    return answer

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 3, 1, 1], [2, 1, 2, 1, 1], [3, 1, 1, 1, 1]]
moves = [1, 1, 1, 3, 3, 3]

print(solution(board,moves))