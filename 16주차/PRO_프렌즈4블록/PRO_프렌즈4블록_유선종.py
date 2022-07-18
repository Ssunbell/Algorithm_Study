def solution(m, n, board):
    board = [list(b) for b in board]
    while True:
        s = []
        for i in range(m):
            if i == m-1:
                break
            for j in range(n):
                if j == n-1:
                    break
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] and board[i][j] != '팡!':
                    s.append([[i,j], [i, j+1], [i+1, j], [i+1, j+1]])
                    
        if not s:
            break
        
        while s:
            pos = s.pop(0)
            for p in pos:
                board[p[0]][p[1]] = '팡!'

        for i in range(m-2, -1, -1):
            for j in range(n):
                if board[i][j] != '팡!':
                    dx = i
                    while True:
                        dx += 1
                        try:
                            if board[dx][j] == '팡!':
                                board[dx][j] = board[dx-1][j]
                                board[dx-1][j] = '팡!'
                            else:
                                break
                        except:
                            break
                        

    answer = 0
    for row in board:
        answer += row.count('팡!')
    return answer

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))