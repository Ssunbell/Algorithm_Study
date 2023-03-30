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

    # def show(self):
    #     print("blue", "green", f"score:{self.score}", sep="\t\t")
    #     for l, r in zip(self.blue, self.green):
    #         print(l,r)

def solve(queries):
    board = MonominoDomino()
    # cnt = 1
    for t,x,y in queries:
        # print(f"round {cnt} | {t}/{x}/{y}")
        # cnt+=1
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
    solve([list(map(int, input().split())) for _ in range(int(input()))])


"""
    단순 구현 문제
    blue, green 모두 6 x 4 Matrix으로 생성
    1. 한 줄이 모두 1인 경우? all([i==1 for i in board[idx]]) => 꽉찬 줄 지우고 점수획득 => board.pop(idx)
    2. 줄에 1이 하나라도 있는 경우? any([i==1 for i in line]) => 스페셜 라인에 블록이 쌓인 경우 => 맨 아래를 지움 => board.pop()
    3. 1,2가 끝나면 zfill느낌으로 배열 길이가 6이 될 때 까지 [0,0,0,0]을 0번 index에 insert 해줌 => board.insert(0, [0,0,0,0])
    4. 블록을 insert 해야 할 경우 insert할 index를 받아오는 함수 = get_top_idx
        4-1. 인자로 받은 인덱스들에 대하여 최상단부터 탐색
        4-2. 하나라도 1이 있으면 (any([i==1 for i in baord[idx]])) idx-1 반환
    5. 블록 insert을 해야 할 경우 삽입하는 함수 = insert_blocks, type은 색깔, idxs는 타겟 인덱스들.
        5-1. get_top_idx로 top_idx 받아오고
        5-2. 해당 위치에 1을 삽입
    6. 블록 insert, blue는 x만, green은 y만 고려하면 됨
        6-1. 타입이 1인 경우 blue, green에 각각 [x], [y] 넣어줌
        6-2. 타입이 2인 경우 가로로 김. blue에 [x]를 두번, green에 [y,y+1] 한번
        6-3. 타입이 3인 경우 세로로 김. blue에 [x,x+1] 한번, green에 [x]를 두번
        6-4. insert 후에는 항상 1, 2를 수행함
"""