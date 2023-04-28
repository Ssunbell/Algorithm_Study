import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from copy import deepcopy

class Game:
    def __init__(self):
        # type, location
        self.players = [[0,0] for _ in range(4)]
        self.history = [[] for _ in range(4)]
        self.blue = set([10,20,30])
        self.board = [
            [i for i in range(0, 42, 2)]+[0],
            [10,13,16,19,25,30,35,40,0],
            [20,22,24,25,30,35,40,0],
            [30,28,27,26,25,30,35,40,0],
        ]
        self.score = 0

    def move(self, player_index, val):
        p_type, p_loc = self.players[player_index]
        n_loc = min(p_loc+val, len(self.board[p_type])-1)
        
        self.score += self.board[p_type][n_loc]
        if p_type==0 and self.board[p_type][n_loc] in (10,20,30):
            self.players[player_index] = [self.board[p_type][n_loc]//10, 0]
        else:
            self.players[player_index][1] = n_loc
        self.history[player_index].append(self.players[player_index][:])
    
    def undo(self, player_index):
        p_type, p_loc = self.players[player_index]
        self.score -= self.board[p_type][p_loc]
        self.history[player_index].pop()
        self.players[player_index] = self.history[player_index][-1]
        
    
    def show(self):
        print("*"*10, self.score, "*"*10)
        print(*[f"player : {i} | location : {self.players[i]}" for i in range(4)], sep="\n", end="\n\n")
        # print(*self.board, sep="\n")

def btk(game, visited, query):
    print(visited)
    global answer
    if len(visited)==10:
        answer = max(answer, game.score)
    else:
        for player_index in range(4):
            for idx, move_type in enumerate(query):
                if idx in visited:
                    continue
                game.move(player_index, move_type)
                visited.add(idx)
                btk(game, visited, query)
                game.undo(player_index)
                visited.remove(idx)

def main():
    global answer
    game = Game()
    dice = list(map(int, input().split()))
    answer = float("inf")
    btk(game, set(), dice)
    print(game)


if __name__ == "__main__":
    main()