import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

class Calculate:
    def __init__(self, N:int):
        '''
        오른쪽으로 합치는 것을 기준으로
        다른 위아래왼쪽을 오른쪽으로 회전, 반전한 후
        합치는 연산을 진행
        '''
        self.N = N
        self.qwer = [[self.rotate_right, self.add, self.rotate_left], # 위
                     [self.rotate_left, self.add, self.rotate_right], # 아래
                     [self.revert, self.add, self.revert], # 왼쪽
                     [self.add]] # 오른쪽
        self.answer = deque([])

    def add(self, array:deque) -> deque:
        numbers = deque([[k for k in arr if k] for arr in array])
        new_array = deque([])
        for row in numbers:
            row = row[::-1]
            for i, n in enumerate(row):
                if i != len(row)-1 and n == row[i+1]:
                    row[i] *= 2
                    row[i+1] = 0
            tmp = [r for r in row if r]
            new_array.append([0] * (self.N - len(tmp)) + tmp[::-1])

        return new_array
    
    def rotate_right(self, array:deque) -> deque:
        return deque([[array[j][i] for j in range(self.N-1, -1, -1)] for i in range(self.N)])
        
    def rotate_left(self, array:deque) -> deque:
        return deque([[array[j][i] for j in range(self.N)] for i in range(self.N-1, -1, -1)])
        
    def revert(self, array:deque) -> deque:
        return deque([[array[i][j] for j in range(self.N-1, -1, -1)] for i in range(self.N)])
        
    def run(self, array:deque, depth:int):
        if depth == 5:
            self.answer.append(max([max(row) for row in array]))
            return
        
        for func in self.qwer:
            array_new = array
            for f in func:
                array_new = f(array_new)
            self.run(array_new, depth + 1)
            
N = int(input())
array = deque([list(map(int, input().split())) for _ in range(N)])
game = Calculate(N)
game.run(array, 0)
print(max(game.answer))