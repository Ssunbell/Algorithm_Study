from collections import deque
from itertools import permutations
import copy

def rotate(b, k, r, c):
    ltop, rtop, rbottom, lbottom = b[r - k][c - k], b[r - k][c + k], b[r + k][c + k], b[r + k][c - k]
    for i in range(2 * k - 1):
        b[r - k + i][c - k] = b[r - k + i + 1][c - k]
        b[r - k][c + k - i] = b[r - k][c + k - i - 1]
        b[r + k - i][c + k] = b[r + k - i - 1][c + k]
        b[r + k][c - k + i] = b[r + k][c - k + i + 1]
    b[r - k][c - k + 1], b[r - k + 1][c + k], b[r + k][c + k - 1], b[r + k - 1][c - k] = ltop, rtop, rbottom, lbottom
    return b

def run(board:list, q:list):
    r, c, s = q
    for k in range(1, s + 1):
        board = rotate(board, k, r - 1, c - 1)
    return board

if __name__ == '__main__':
    answer = float('inf')
    n, m, k = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    query_ = [list(map(int, input().split())) for _ in range(k)]
    for query in permutations(query_):
        board = copy.deepcopy(b)
        for q in query:
            board = run(board, q)
        for a in board:
            answer = min(answer, sum(a))
    print(answer)