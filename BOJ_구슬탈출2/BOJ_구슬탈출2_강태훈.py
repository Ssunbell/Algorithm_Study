import sys
from copy import deepcopy
from collections import deque
input = lambda : sys.stdin.readline().strip()

class EscapeBoard:
    def __init__(self, n, m, board, loc_info):
        self.dx = [0,1,0,-1]
        self.dy = [-1,0,1,0]
        self.board = board
        self.n, self.m = n, m
        self.R, self.B, self.O = [loc_info[i] for i in "RBO"]
    
    def _move(self, target, direction):
        up_target = self.B if target=="B" else self.R
        x, y = up_target
        while self.board[(x+self.dx[direction], y+self.dy[direction])] ==".":
            x, y = x+self.dx[direction], y+self.dy[direction]
        if self.board[(x+self.dx[direction], y+self.dy[direction])] == "O":
            x, y = x+self.dx[direction], y+self.dy[direction]
            self.board[(x,y)] = "."
            self.board[up_target] = "O"
        self.board[(x,y)], self.board[up_target] = self.board[up_target], self.board[(x,y)]
        up_target = (x,y)
        if target == "B" : self.B = (x,y)
        elif target == "R" : self.R = (x,y)
    
    def move(self, direction):
        rx, ry = self.R
        bx, by = self.B
        if rx==bx and direction == 0:
            if ry < by : seq = "RB"
            else : seq = "BR"
        elif rx==bx and direction == 2:
            if ry > by : seq = "RB"
            else : seq = "BR"
        elif ry==by and direction == 1:
            if rx > bx : seq = "RB"
            else : seq = "BR"
        elif ry==by and direction == 3:
            if rx < bx : seq = "RB"
            else : seq = "BR"
        else: seq = "BR"
        for target in seq:
            self._move(target, direction)
        return ((rx,ry) != self.R or (bx, by) != self.B) and (self.B!=self.O)

        
def solve(n, m, board, loc_info):
    init_board = EscapeBoard(n,m,board,loc_info)
    q = deque([(init_board, 0, [])])
    visited = set()
    visited.add((init_board.R,init_board.B, -1))
    while q:
        board, cnt, history = q.popleft()
        for i in range(4):
            new_board = deepcopy(board)
            avaliable = new_board.move(i)
            if (new_board.R, new_board.B, i) in visited or new_board.B == new_board.O:
                continue
            if new_board.R == new_board.O:
                return cnt+1
            if cnt == 10:
                return -1
            if avaliable:
                q.append((new_board, cnt+1, history[:]+[i]))
                visited.add((new_board.R, new_board.B, i))
    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = {}
    loc_info = {i:[] for i in ".#ORB"}
    for i in range(n):
        line = input()
        for j, val in enumerate(line):
            board[(j,i)] = val
            loc_info[val].append((j,i))
            
    print(solve(n, m, board, {i:loc_info[i][0] for i in "RBO"}))