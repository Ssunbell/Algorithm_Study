from collections import deque

move = [(1,0,1,0),(0,1,0,1),(-1,0,-1,0),(0,-1,0,-1)]
turn = [
    [(1,-1,0,0),(0,0,-1,-1),(0,0,-1,1),(1,1,0,0)],
    [(-1,1,0,0),(1,1,0,0),(0,0,1,-1),(0,0,-1,-1)]
]
get_side = lambda a,b,c : (a[0]^b[0]^c[0], a[1]^b[1]^c[1])

def get_near(n, board, robot_loc, cdir):
    for diff in move:
        nloc = tuple(map(sum, zip(robot_loc, diff)))
        nx1, ny1, nx2, ny2 = nloc
        if all([0<=i<n for i in nloc]) and board[ny1][nx1]==0 and board[ny2][nx2]==0:
            yield tuple(sum(sorted([[nx1, ny1], [nx2,ny2]]),[]))
    for diff in turn[cdir]:
        nloc = tuple(map(sum, zip(robot_loc, diff)))
        nx1, ny1, nx2, ny2 = nloc
        if all([0<=i<n for i in nloc]) and board[ny1][nx1]==0 and board[ny2][nx2]==0:
            side_x, side_y = get_side(*list(set([nloc[:2], nloc[-2:], robot_loc[:2], robot_loc[-2:]])))
            if board[side_y][side_x]==0:
                yield tuple(sum(sorted([[nx1, ny1], [nx2,ny2]]),[]))

def solution(board):
    n = len(board)
    q = deque([[0, (0,0,1,0)]])
    visited = set([(0,0,1,0)])

    while q:
        cnt, cloc = q.popleft()
        for nloc in get_near(n, board, cloc, 0 if cloc[1]==cloc[3] else 1):
            if (n-1,n-1) in (nloc[:2], nloc[-2:]):
                return cnt+1
            if nloc not in visited:
                q.append([cnt+1, nloc])
                visited.add(nloc)
    return -1