import sys
input = sys.stdin.readline

class Cubic:
    def __init__(self):
        self.cubic = {
            "U":[["w"]*3 for _ in range(3)], 
            "D":[["y"]*3 for _ in range(3)], 
            "F":[["r"]*3 for _ in range(3)], 
            "B":[["o"]*3 for _ in range(3)], 
            "L":[["g"]*3 for _ in range(3)], 
            "R":[["b"]*3 for _ in range(3)],
        }
        self.rot_info = {
            "U":{"B":0,     "R":180,    "F":180,    "L":180,},
            "D":{"F":0,     "R":0,      "B":180,    "L":0,},
            "F":{"U":0,     "R":270,    "D":180,    "L":90,},
            "B":{"D":0,     "R":90,     "U":180,    "L":270,},
            "L":{"U":270,   "F":270,    "D":270,    "B":270,},
            "R":{"U":90,    "B":90,     "D":90,     "F":90,},
        }

    def lot_surface(self, surface, degree=90):
        if degree == 90:
            self.cubic[surface] = [i[::-1] for i in zip(*self.cubic[surface])]
        elif degree == 180:
            self.cubic[surface] = [i[::-1] for i in self.cubic[surface]][::-1]
        elif degree == 270:
            self.cubic[surface] = [i for i in zip(*self.cubic[surface])][::-1]

    def process(self, rot_seq):
        tmp = self.cubic[rot_seq[3]].pop()
        for i in range(3,0,-1):
            l, r = rot_seq[i], rot_seq[i-1]
            self.cubic[l].append(self.cubic[r].pop())
        self.cubic[rot_seq[0]].append(tmp)

    def rot90(self, surface):
        surface_rot_info = self.rot_info[surface]
        for s, d in surface_rot_info.items():
            self.lot_surface(s,d)

        self.process(list(surface_rot_info.keys()))
        self.lot_surface(surface)
        for s, d in surface_rot_info.items():
            self.lot_surface(s, 360-d)

    def turn(self, surface, method):
        for _ in range(1 if method=="+" else 3):
            self.rot90(surface)

    def print(self, surface="U"):
        for l in self.cubic[surface]:
            print(*l, sep="")

if __name__=="__main__":
    n = int(input())
    for tc in range(n):
        _ = input()
        cubic = Cubic()
        for cmd in input().split():
            cubic.turn(*list(cmd))
        cubic.print()

""" 먼저, 
    U
L   F   R
    D
    B
형태로 면을 표현 => self.cubic """

# 회전시켜도 큐빅 line 속 원소의 순서는 변하지 않는다는 점을 활용
# 회전시키기 전에 인접한 면 의 방향을 Bottom으로 일치키고, pop, append로 한번에 돌린 후 원상복구
""" 예를들어,
    123
    456
    789 
    에서 963에 회전을 적용하고 싶다면 배열을 90도 회전시켜
    
    741
    852
    963 
    형태로 변경 후, pop을 진행하면 963이 뽑힌다. 해당 자리에 000을 넣는다고 하면

    741
    852
    000 
    이 되고, 360 - 90 = 270도 회전을 적용시키면

    120
    450
    780 
    으로 회전 연산이 완료된다. """


""" 회전량 계산 방법
        U
    L   F   R
        D
        B
    도면에서 기준면 a와 비교면 b에서 b의 *아래쪽*이 a와 붙어있으면 *Bot*  :    0
    도면에서 기준면 a와 비교면 b에서 b의 *오른쪽*이 a와 붙어있으면 *Right*  :  90
    도면에서 기준면 a와 비교면 b에서 b의 *윗쪽*이 a와 붙어있으면 *Top*  :     180
    도면에서 기준면 a와 비교면 b에서 b의 *왼쪽*이 a와 붙어있으면 *Left*  :    270
    
    예를들어, 
    기준면 F와 비교면 L에서 L의 오른쪽이 F와 붙어있으니 Right -> 90도 회전
    기준면 F와 비교면 R에서 R의 왼쪽이 F와 붙어있으니 Left -> 270도 회전
    기준면 F와 비교면 D에서 D의 윗쪽이 F와 붙어있으니 Top -> 180도 회전
    기준면 F와 비교면 U에서 U의 아래쪽이 F와 붙어있으니 Bot -> 180도 회전 """

""" 모든 면의 맨 아래를 시계방향으로 회전시킴. rot_info의 길이는 4로, 회전방향으로 이동하며 그 순서대로 딕셔너리 rot_info의 key를 세팅 -> key에 해당하는 value는 위에서 구한 회전량
    F를 회전시킨다고 하면 rot_info의 key는 U,R,D,L
    tmp = L에서 pop                     [3]
    L에 D pop, D에 R pop, R에 U pop     [3,2], [2,1], [1,0]
    U에 tmp                             [0]
    이런식으로 pop과 append만으로 구현이 가능하다. """