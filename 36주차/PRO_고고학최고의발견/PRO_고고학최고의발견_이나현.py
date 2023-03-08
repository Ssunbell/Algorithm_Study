#프로그래머스_고고학 최고의 발견
from itertools import product
import copy

def turn_needle(i, j, cnt):
    global table
    pos = [(i-1,j), (i,j-1), (i,j), (i,j+1), (i+1,j)]
    for r,c in pos:
        table[r][c] = (table[r][c] + cnt) % 4
    return

def solution(clockHands):
    global table
    side_len = len(clockHands[0])
    table_origin = [[0] * (side_len + 2)] + \
            [[0] + row + [0] for row in clockHands] + \
            [[0] * (side_len + 2)]
    items = [[0,1,2,3] for _ in range(side_len)]
    first_row_case = list(product(*items))
    answer_min = 1e9
    for case in first_row_case:          #첫재 줄에 대해선 완전탐색
        table = copy.deepcopy(table_origin)
        answer = 0
        for j in range(side_len):
            if case[j]:
                turn_needle(1, j+1, case[j])
                answer += case[j]
        for i in range(2, side_len+1):   #둘째 줄부터 마지막 줄까지
            for j in range(1, side_len+1):
                if table[i-1][j]:
                    answer += 4-table[i-1][j]
                    turn_needle(i, j, 4-table[i-1][j])
        for j in range(1, side_len+1):   #마지막 줄에 값이 남았는지 확인. 남았으면 해당 first_row_case가 정답이 아님
            if table[side_len][j]:
                break
        else:
            answer_min = min(answer, answer_min)
    return answer_min

print(solution([[0, 3, 3, 0], [3, 2, 2, 3], [0, 3, 2, 0], [0, 3, 3, 3]]))
print(solution([[2,2,1,1],[2,0,0,1],[0,0,0,3],[2,0,3,1]]))