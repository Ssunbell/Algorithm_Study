#[프로그래머스_행렬과 연산]
from collections import deque

def solution(rc, operations):

    def shiftrow():
        left_col.appendleft(left_col.pop())
        right_col.appendleft(right_col.pop())
        mid_col.appendleft(mid_col.pop())

    def rotate():
        mid_col[0].appendleft(left_col.popleft())
        right_col.appendleft(mid_col[0].pop())
        mid_col[-1].append(right_col.pop())
        left_col.append(mid_col[-1].popleft())

    row_len = len(rc)
    left_col = deque([rc[i][0] for i in range(row_len)])
    right_col = deque([rc[i][-1] for i in range(row_len)])
    mid_col = deque([deque(rc[i][1:-1]) for i in range(row_len)])

    for o in operations:
        if o == "ShiftRow":
            shiftrow()
        elif o == "Rotate":
            rotate()
    
    left_col = list(left_col)
    mid_col = [list(mid_col[i]) for i in range(row_len)]
    right_col = list(right_col)

    result = [list([left_col[i]]+mid_col[i]+[right_col[i]]) for i in range(row_len)]
    return result

'''
# 효율성 5/9 통과
def solution(rc, operations):

    def shiftrow():
        last_row = answer.pop()
        answer.appendleft(last_row)

    def rotate(row_len):
        for i in range(1, row_len):
            up = answer[i].popleft()
            answer[i-1].appendleft(up)
        for i in range(row_len-2, -1, -1):
            down = answer[i].pop()
            answer[i+1].append(down)
        return answer

    answer = deque()
    for row in rc:
        answer.append(deque(row))
    row_len = len(answer)
    for oper in operations:
        if oper == "ShiftRow":
            shiftrow()
        elif oper == "Rotate":
            answer = rotate(row_len)
    for i in range(row_len):
        answer[i] = list(answer[i])
    answer = list(answer)
    return answer
'''
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
print(solution(	[[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))

# 1 2 3 4
# 5 6 7 8
# 9 A B C
# D E F G