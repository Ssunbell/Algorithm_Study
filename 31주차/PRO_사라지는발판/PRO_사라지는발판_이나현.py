#[프로그래머스_사라지는발판]
from collections import defaultdict
from copy import deepcopy

def brute_recur(board, aloc, bloc, AB, cnt):
    h = len(board)
    w = len(board[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = [None, None]
    min_cnt, max_cnt = 1e9, 0

    if AB == 'A':
        x, y = aloc
        if board[x][y] == 0: #현재 위치가 사라진 발판
            return (['B', cnt])
        flag = 0
        for k in range(4):
            if 0 <= x + dx[k] < h and 0 <= y + dy[k] < w and board[x+dx[k]][y+dy[k]]:
                flag = 1
                board2 = deepcopy(board)
                board2[x][y] = 0
                board2[x+dx[k]][y+dy[k]] = 2
                winner, result_cnt = brute_recur(board2, [x+dx[k],y+dy[k]], bloc, 'B', cnt+1)
                if winner == 'A':
                    min_cnt = min(min_cnt, result_cnt)
                    result = ['A', min_cnt]
                else:
                    max_cnt = max(max_cnt, result_cnt)
        if flag == 0: #갈 곳이 없는 경우
            return ['B', cnt]

        if result[0] == None:
            return ['B', max_cnt]
        return result

    elif AB =='B':
        x, y = bloc
        if board[x][y] == 0: #현재 위치가 사라진 발판
            return (['A', cnt])
        flag = 0
        for k in range(4):
            if 0 <= x + dx[k] < h and 0 <= y + dy[k] < w and board[x+dx[k]][y+dy[k]]:
                flag = 1
                board2 = deepcopy(board)
                board2[x][y] = 0
                board2[x+dx[k]][y+dy[k]] = 2
                winner, result_cnt = brute_recur(board2, aloc, [x+dx[k],y+dy[k]], 'A', cnt+1)
                if winner == 'B':
                    min_cnt = min(min_cnt, result_cnt)
                    result = ['B', min_cnt]
                else:
                    max_cnt = max(max_cnt, result_cnt)
        if flag == 0: #갈 곳이 없는 경우
            return ['A', cnt]

        if result[0] == None:
            return ['A', max_cnt]
        return result
    
def solution(board, aloc, bloc):
    return(brute_recur(board, aloc, bloc, 'A', 0)[1])



'''
# 정확도 50점
# 해당 위치에서 움직일 수 있는 모든 경우의 결과를 저장해둠
# result를 모아서 만약 A가 이기는 경우, B가 이기는 경우가 모두 있다 -> 승리를 보장할 수 없는 움직임이므로 None을 return 하는 방법

def brute_recur(board, aloc, bloc, AB, cnt):
    h = len(board)
    w = len(board[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    results = []
    if AB == 'A':
        x, y = aloc
        if board[x][y] == 0:
            return (['B', cnt])
        flag = 0
        for k in range(4):
            if 0 <= x + dx[k] < h and 0 <= y + dy[k] < w and board[x+dx[k]][y+dy[k]]:
                flag = 1
                board2 = deepcopy(board)
                board2[x][y] = 0
                board2[x+dx[k]][y+dy[k]] = 2
                winner, result_cnt = brute_recur(board2, [x+dx[k],y+dy[k]], bloc, 'B', cnt+1)
                results.append([winner, result_cnt])
        if flag == 0: #갈 곳이 없는 경우
            return ['B', cnt]

        result = results[0]
        for i in range(1, len(results)):
            if results[i][0] == None:
                continue
            # if cnt > 1 and (results[i][0] != result[0]): #결과에 A와 B 둘다 이기는 경우가 있을 때
            #     result = [None, None]
            #     break
            if results[i][0] == 'A':
                result[1] = min(result[1], results[i][1])
            elif results[i][0] == 'B':
                result[1] = max(result[1], results[i][1])
        return result

    if AB =='B':
        x, y = bloc
        if board[x][y] == 0:
            return (['A', cnt])
        flag = 0
        for k in range(4):
            if 0 <= x + dx[k] < h and 0 <= y + dy[k] < w and board[x+dx[k]][y+dy[k]]:
                flag = 1
                board2 = deepcopy(board)
                board2[x][y] = 0
                board2[x+dx[k]][y+dy[k]] = 2
                winner, result_cnt = brute_recur(board2, aloc, [x+dx[k],y+dy[k]], 'A', cnt+1)
                results.append([winner, result_cnt])
        if flag == 0: #갈 곳이 없는 경우
            return ['A', cnt]

        result = results[0]
        for i in range(1, len(results)):
            if results[i][0] == None:
                continue
            # if cnt > 2 and (results[i][0] != result[0]): #결과에 A와 B 둘다 이기는 경우가 있을 때
            #     result = [None, None]
            #     break
            if results[i][0] == 'B':
                result[1] = min(result[1], results[i][1])
            elif results[i][0] == 'A':
                result[1] = max(result[1], results[i][1])
        return result
    
def solution(board, aloc, bloc):
    return(brute_recur(board, aloc, bloc, 'A', 0)[1])
'''
print(solution(	[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2])) #5
print(solution(	[[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2])) #4
print(solution(	[[1, 1, 1, 1, 1]], [0, 0], [0, 4])) #4
print(solution(	[[1]], [0, 0], [0, 0])) #0