from typing import *

class WeightedUF():
    def __init__(self):
        self.parent = [[[-1, -1] for _ in range(51)] for _ in range(51)]
        
    def find(self, r:int, c:int) -> List[int]:
        if self.parent[r][c][0] < 0 and self.parent[r][c][1] < 0:
            return [r, c]
        else:
            r2, c2 = self.find(*self.parent[r][c])
            self.parent[r][c] = [r2, c2]
            return [r2, c2]
        
    def union(self, r1, c1, r2, c2):
        r1, c1 = self.find(r1, c1)
        r2, c2 = self.find(r2, c2)
        
        if [r1, c1] == [r2, c2]: return
        
        r1_r, c1_r = self.parent[r1][c1]
        r2_r, c2_r = self.parent[r2][c2]
        
        if (r1_r + c1_r) <= (r2_r + c2_r):
            self.parent[r1][c1] = [r1_r + r2_r, c1_r + c2_r]
            self.parent[r2][c2] = [r1, c1]
        else:
            self.parent[r2][c2] = [r1_r + r2_r, c1_r + c2_r]
            self.parent[r1][c1] = [r2, c2]

class Table(WeightedUF):
    def __init__(self): 
        super().__init__()
        self.table = [[''] * 51 for _ in range(51)]
    
    def update_value_another_value(self, value1:str, value2:str):
        for i in range(51):
            for j in range(51):
                if self.table[i][j] == value1:
                    self.table[i][j] = value2
    
    def update_point_value(self, r:int, c:int, value:str):
        self.table[r][c] = value
        if self.parent[r][c] != [-1, -1]:
            r, c = self.find(r, c)
            for i in range(51):
                for j in range(51):
                    if self.find(i,j) == [r, c]:
                        self.table[i][j] = value
    
    def merge_values(self, r1, c1, r2, c2):
        self.union(r1, c1, r2, c2)
        value = self.table[r1][c1] if self.table[r1][c1] else self.table[r2][c2]
        self.update_point_value(r1, c1, value)
        
    def unmerge_values(self, r, c):
        r1, c1 = self.find(r, c)
        value = self.table[r][c]
        for i in range(51):
            for j in range(51):
                if self.find(i, j) == [r1, c1]:
                    self.parent[i][j] = [-1, -1]
                    self.table[i][j] = ''
        self.parent[r][c] = [-1, -1]
        self.table[r][c] = value

    def print_value(self, r:int, c:int) -> str:
        if self.table[r][c]:
            return self.table[r][c]
        else:
            return 'EMPTY'

def solution(commands):
    answer = []
    uf = Table()
    for command in commands:
        com = command.split()
        if com[0] == 'UPDATE':
            if len(com) == 4:
                r, c, value = int(com[1]),int(com[2]),com[3]
                uf.update_point_value(r, c, value)
            elif len(com) == 3:
                value1, value2 = com[1], com[2]
                uf.update_value_another_value(value1, value2)
        elif com[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, [com[1],com[2],com[3],com[4]])
            uf.merge_values(r1, c1, r2, c2)
        elif com[0] == 'UNMERGE':
            r, c = map(int, [com[1],com[2]])
            uf.unmerge_values(r, c)
        elif com[0] == 'PRINT':
            r, c = map(int, [com[1],com[2]])
            answer.append(uf.print_value(r, c))

    return answer