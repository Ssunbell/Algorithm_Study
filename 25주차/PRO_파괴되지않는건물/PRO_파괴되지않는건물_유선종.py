def cumulative_sum(row:int, col:int, cumul:list) -> list:
    # 행 기준 누적합
    for r in range(row-1):
        for c in range(col-1):
            cumul[r][c + 1] += cumul[r][c]

    # 열 기준 누적합
    for r in range(row-1):
        for c in range(col-1):
            cumul[r + 1][c] += cumul[r][c]
    
    cumul = [r[:col-1] for r in cumul[:row-1]]
    
    yield from cumul

def solution(board:list, skill:list) -> int:

    # 누적합을 기록하기 위한 배열, 기존 배열보다 길이가 1씩 더 많아야함
    col = len(board[0]) + 1
    row = len(board) + 1
    cumul = [[0] * col for _ in range(row)]
    for command in skill:
        t, r1, c1, r2, c2, degree = command
        
        cumul[r1][c1] += degree if t == 2 else (-1) * degree
        cumul[r1][c2 + 1] -= degree if t == 2 else (-1) * degree
        cumul[r2 + 1][c1] -= degree if t == 2 else (-1) * degree
        cumul[r2 + 1][c2 + 1] += degree if t == 2 else (-1) * degree

    answer = 0
    # 제너레이터 객체를 쓰면 적게는 5ms, 많게는 50ms의 시간이 절약됨
    cumulation = cumulative_sum(row, col, cumul)
    for r, row in enumerate(cumulation):
        for c, value in enumerate(row):
            if (board[r][c] + value) > 0:
                answer += 1
            
    return answer