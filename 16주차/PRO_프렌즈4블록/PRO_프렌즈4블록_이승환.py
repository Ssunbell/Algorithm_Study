def solution(m, n, board):
    answer = 0
    board_new = [[0]*m for _ in range(n)]
    for j in range(m):
        for i in range(n):
            board_new[i][j] = board[j][i]
    while True:
        boom = set()
        
        # 폭파할 경우 찾기
        for i in range(n-1):
            for j in range(m-1):
                friend = board_new[i][j]
                if board_new[i+1][j] == friend and board_new[i][j+1] == friend and board_new[i+1][j+1] == friend:
                    boom.add((i,j))
                    boom.add((i+1,j))
                    boom.add((i,j+1))
                    boom.add((i+1,j+1))
        
        # 폭파, 하나씩 빼면 안되는데 동시에 빼면 됨.
        boom = sorted(boom,reverse=True)
        for blank in boom:
            i,j = blank
            del board_new[i][j]
            answer += 1
        

        if answer > 3:
            break
    return answer

board_new = 	["CCBDE", "AAADE", "AAABF", "CCBBF"]

print(solution(4,5,board_new))

