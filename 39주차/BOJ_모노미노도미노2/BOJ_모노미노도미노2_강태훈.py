import sys
input =  sys.stdin.readline

class MonominoDomino:
    def __init__(self):
        self.blue = [[0]*4 for i in range(6)]
        self.green = [[0]*4 for i in range(6)]
        self.score = 0
    
    def clear_line(self, target):
        clear_target = self.blue if target=="b" else self.green
        clear_idx = [idx for idx,vals in enumerate(clear_target) if all([i==1 for i in vals])]
        for idx in clear_idx[::-1]:
            clear_target.pop(idx)
            self.score += 1
        for _ in clear_idx:
            clear_target.insert(0,[0,0,0,0])
    
    def get_top_idx(self, target, idxs):
        insert_target = self.blue if target=="b" else self.green
        for i in range(6):
            if any([insert_target[i][idx]==1 for idx in idxs]):
                return i-1
        return 5

    def activate_special_blocks(self, target):
        activate_target = self.blue if target=="b" else self.green
        for vals in activate_target[:2]:
            if sum(vals)>0:
                activate_target.pop()
                activate_target.insert(0,[0,0,0,0])
    
    def insert_blocks(self, target, idxs):
        insert_target = self.blue if target=="b" else self.green
        top_idx = self.get_top_idx(target, idxs)
        if top_idx == -1:
            ...
        else:
            for i in idxs:
                insert_target[top_idx][i] = 1
        self.clear_line(target)
        self.activate_special_blocks(target)
    
    def answer(self):
        print(self.score)
        print(sum(sum(self.green, []))+sum(sum(self.blue, [])))

    def show(self):
        print("blue", "green", f"score:{self.score}", sep="\t\t")
        for l, r in zip(self.blue, self.green):
            print(l,r)

def solve(n, queries):
    board = MonominoDomino()
    cnt = 1
    for t,x,y in queries:
        # print(f"round {cnt} | {t}/{x}/{y}")
        cnt+=1
        if t==1:
            board.insert_blocks("b",[x])
            board.insert_blocks("g",[y])
        elif t==2:
            board.insert_blocks("b",[x])
            board.insert_blocks("b",[x])
            board.insert_blocks("g",[y,y+1])
        elif t==3:
            board.insert_blocks("b",[x,x+1])
            board.insert_blocks("g",[y])
            board.insert_blocks("g",[y])
        # board.answer()
        # board.show()
    board.answer()

if __name__ == "__main__":
    n = int(input())
    solve(n, [list(map(int, input().split())) for _ in range(n)])
