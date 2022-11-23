"""
풀이 방향성 잡기:
    1. n이 작기 때문에 완전탐색이 가능하다.
    2. 한쪽 방향에 대한 구현만을 하면 된다. 
    (따라서 구현하기 편한 방향이 뭔지 생각해보자)
    3. 나머지 세 방향에 대해서는 기준 방향으로 바꾼 다음에 다시 되돌리면 된다.
    4. 5회째 이동 됐을 때에 answer 리스트에 최대값을 저장한다.
    5. 최종적으로 답은 answer 리스트의 최대값을 반환한다.
"""

import sys
input = sys.stdin.readline

n = int(input().strip())
b = [list(map(int, input().split())) for _ in range(n)]

global answer
answer = []

# 오른쪽에서 왼쪽으로 push하는 연산
# board: 2차원 리스트
def push(board:list):
    res = []
    for row in board:
        arr = [val for val in row if val]
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                arr[i] *= 2
                arr[i + 1] = 0
        arr = [val for val in arr if val]
        res.append(arr + [0] * (n - len(arr)))
    return res

def right_90_turn(board:list):
    return list(map(list, zip(*board)))[::-1]

def left_90_turn(board:list):
    return list(map(list, zip(*board[::-1])))

def reverse(board:list):
    return [row[::-1] for row in board]

# 0: 왼쪽으로, 1: 오른쪽으로, 2: 위쪽으로, 3: 아래쪽으로
direction = [[push],
             [reverse, push, reverse],
             [left_90_turn, push, right_90_turn],
             [right_90_turn, push, left_90_turn]]

# level: dfs 깊이
def dfs(level:int, board:list):
    global answer
    if level == 5:
        answer.append(max(max(row) for row in board))
        return
    else:
        # 4방향 탐색
        for i in range(4):
            tmp = board[:]
            for convert in direction[i]:
                tmp = convert(tmp)
            dfs(level + 1, tmp)

def solution(n, board):
    dfs(0, board)
    return max(answer)

print(solution(n, b))