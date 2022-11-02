from collections import deque
    
def solution(rc, operations):
    '''
    left  center right
      d   deque1   d 
      e   deque2   e
      q   deque3   q
      u   deque4   u
      e   deque5   e
    '''
    rc = deque(rc)
    inner_matrix = deque([])
    first_col = deque([])
    last_col = deque([])
    for row in rc:
        inner_matrix.append(deque(row[1:-1]))
        first_col.append(row[0])
        last_col.append(row[-1])
    for command in operations:
        if command == 'ShiftRow':
            inner_matrix.appendleft(inner_matrix.pop())
            first_col.appendleft(first_col.pop())
            last_col.appendleft(last_col.pop())
        else:
            # 왼쪽 위를 오른쪽으로 shift
            inner_matrix[0].appendleft(first_col.popleft())
            # 오른쪽 위를 아래로 shift
            last_col.appendleft(inner_matrix[0].pop())
            # 오른쪽 아래를 왼쪽으로 shift
            inner_matrix[-1].append(last_col.pop())
            # 왼쪽 아래를 위로 shift
            first_col.append(inner_matrix[-1].popleft())

    answer = [[f] + list(row) + [l] 
              for f, row, l in zip(first_col, inner_matrix, last_col)]
    
    return answer