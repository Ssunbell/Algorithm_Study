# 2차원 누적합
def solution(board, skill):
    answer = 0
    type_dict = {1: -1, 2: 1}
    n, m = len(board), len(board[0])
    skill_result = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for skill_type, r1, c1, r2, c2, degree in skill:
        degree *= type_dict[skill_type]
        skill_result[r1][c1] += degree
        skill_result[r1][c2 + 1] += -degree
        skill_result[r2 + 1][c1] += -degree
        skill_result[r2 + 1][c2 + 1] += degree

    for i in range(1, n):
        for j in range(m):
            skill_result[i][j] += skill_result[i-1][j]
    for i in range(n):
        for j in range(1, m):
            skill_result[i][j] += skill_result[i][j-1]
            if skill_result[i][j] + board[i][j] > 0:
                answer += 1
    for i in range(n):
        if skill_result[i][0] + board[i][0] > 0:
            answer += 1
    return answer


# itertools의 accumulate 활용
'''
from itertools import accumulate

def solution(board, skill):
    answer = 0
    type_dict = {1: -1, 2: 1}
    n, m = len(board), len(board[0])
    skill_result = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for skill_type, r1, c1, r2, c2, degree in skill:
        degree *= type_dict[skill_type]
        skill_result[r1][c1] += degree
        skill_result[r1][c2 + 1] += -degree
        skill_result[r2 + 1][c1] += -degree
        skill_result[r2 + 1][c2 + 1] += degree
    skill_result = [list(accumulate(l)) for l in skill_result]
    skill_result = [list(accumulate(l)) for l in zip(*skill_result)]
    for i in range(n):
        for j in range(m):
            if skill_result[j][i] + board[i][j] > 0:
                answer += 1
    return answer
'''
# numpy의 cumsum 활용
'''
import numpy as np
def solution(board, skill):
    skill_type = {1: -1, 2: 1}
    field = np.array(board)
    n, m = field.shape
    skill_result = np.zeros(n*m + n + m + 1).reshape(n+1, m+1)

    for _type, r1, c1, r2, c2, degree in skill:
        degree *= skill_type[_type]
        skill_result[r1, c1] += degree
        skill_result[r1, c2+1] += -degree
        skill_result[r2+1, c1] += -degree
        skill_result[r2+1, c2+1] += degree

    skill_result = skill_result.cumsum(axis=0)
    skill_result = skill_result.cumsum(axis=1)
    field = field + skill_result[:-1,:-1]
    answer = len(field[field > 0])
    return answer
'''
