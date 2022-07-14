
def solution(board, moves):
    basket = [] # 인형을 담을 바구니
    answer = 0 # 갯수를 셀 변수
    
    for move in moves:
        for column in board:

            if column[move-1] != 0: 
                basket.append(column[move-1])
                column[move-1] = 0

                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop(-1)
                        basket.pop(-1)
                        answer += 2
                break 
    return answer