from copy import deepcopy

class cell(object):
    def __init__(self):
        self.cells = [[''] * 50 for _ in range(50)]
        self.before_cells = deepcopy(self.cells)
        self.merged = {} # (r, c) : [해당 병합에 속한 (x, y)들 모음]
    def update1(self, r, c, value):
        if (r, c) in self.merged.keys(): # (r, c)가 이전에 병합된 적이 있으면
            for loc in self.merged[(r, c)]:
                self.cells[loc[0]][loc[1]] = value
        else:
            self.cells[r][c] = value
            self.before_cells[r][c] = value
    def update2(self, value1, value2):
        if value1 == value2:
            return
        for r in range(50):
            for c in range(50):
                if self.cells[r][c] == value1:
                    if (r, c) in self.merged.keys(): # 병합된 적이 있으면
                        for loc in self.merged[(r, c)]:
                            self.cells[loc[0]][loc[1]] = value2
                    else:
                        assert self.cells[r][c] == self.before_cells[r][c]
                        self.cells[r][c] = value2
                        self.before_cells[r][c] = value2
    def merge(self, r1, c1, r2, c2): # before_cells는 여기서 사용 x
        def m(r1, c1, r2, c2):
            if (r1, c1) in self.merged.keys() and (r2, c2) in self.merged.keys(): # 둘 다 병합된 적 있는 경우(병합은 따로 된 상황임)
                for loc in self.merged[(r2, c2)]: # (r2, c2)의 병합된 셀들을 모두 (r1, c1)으로 바꾸기
                    self.cells[loc[0]][loc[1]] = self.cells[r1][c1]
                merged_result = []
                for loc in self.merged[(r1, c1)]: # (r1, c1)이 포함하는 셀들에 병합 적용
                    if loc != (r1, c1):
                        self.merged[loc].extend(self.merged[(r2, c2)])
                        if not merged_result:
                            merged_result = self.merged[loc]
                self.merged[(r1, c1)] = merged_result
                for loc in self.merged[(r1, c1)]:
                    self.merged[loc] = merged_result
            elif (r1, c1) in self.merged.keys(): # 이전에 (r1, c1)만 병합된 적이 있는 경우
                self.merged[(r1, c1)].append((r2, c2))
                self.merged[(r2, c2)] = self.merged[(r1, c1)][:]
                self.cells[(r2, c2)] = self.cells[(r1, c1)]
            elif (r2, c2) in self.merged.keys(): # 이전에 (r2, c2)만 병합된 적이 있는 경우
                for loc in self.merged[(r2, c2)]: # (r2, c2)의 병합된 셀들을 모두 (r1, c1)으로 바꾸기
                    self.cells[loc[0]][loc[1]] = self.cells[r1][c1]
                self.merged[(r1, c1)].append((r1, c1))
                self.merged[(r1, c1)] = self.merged[(r2, c2)][:]
            else: # 두 셀 모두 병합된 적 없는 경우
                self.merged[(r1, c1)] = [(r1, c1), (r2, c2)]
                self.merged[(r2, c2)] = [(r1, c1), (r2, c2)]
        if self.cells[r1][c1] == self.cells[r2][c2]:
            return
        if self.cells[r1][c1] != '':
            self.cells[r2][c2] = self.cells[r1][c1]
            m(r1, c1, r2, c2)
        else: # (r1, c1)이 빈 셀인 경우
            self.cells[r1][c1] = self.cells[r2][c2]
            m(r2, c2, r1, c1)


    def merge(self, r1, c1, r2, c2): # before_cells는 여기서 사용 x
        def m(r1, c1, r2, c2): # (r1, c1) 기준으로 값을 바꿈
            if (r1, c1) in self.merged.keys() and (r2, c2) in self.merged.keys(): # 둘 다 병합된 적 있는 경우(병합은 따로 된 상황임)
                for loc in self.merged[(r2, c2)]: # (r2, c2)의 병합된 셀들을 모두 (r1, c1)으로 바꾸기
                    self.cells[loc[0]][loc[1]] = self.cells[r1][c1]
                merged_result = [] # 병합 결과
                for loc in self.merged[(r1, c1)]: # (r1, c1)와 병합된 셀들에 병합 적용
                    self.merged[loc].extend(self.merged[(r2, c2)])
                    if not merged_result: # 병합 결과는 한번만 받으면 됨.
                        merged_result = self.merged[loc]
                for loc in self.merged[(r2, c2)]: # (r2, c2)와 병합된 셀들에 병합 적용
                    self.merged[loc] = merged_result
            elif (r1, c1) in self.merged.keys(): # 이전에 (r1, c1)만 병합된 경우
                val =  self.cells[r1][c1]
                merged_result = self.merged[(r1, c1)] + [(r2, c2)]
                for loc in merged_result:
                    self.merged[loc] = merged_result
                    self.cells[loc[0]][loc[1]] = val
            elif (r2, c2) in self.merged.keys(): # 이전에 (r2, c2)만 병합된 경우
                val =  self.cells[r1][c1]
                merged_result = self.merged[(r2, c2)] + [(r1, c1)]
                for loc in merged_result:
                    self.merged[loc] = merged_result
                    self.cells[loc[0]][loc[1]] = val
            else: # 두 셀 모두 병합된 적 없는 경우
                self.merged[(r1, c1)] = [(r1, c1), (r2, c2)]
                self.merged[(r2, c2)] = [(r1, c1), (r2, c2)]
                self.cells[r2][c2] = self.cells[r1][c1]
        if self.cells[r1][c1] == self.cells[r2][c2]:
            return
        if self.cells[r1][c1] != '':
            m(r1, c1, r2, c2)
        else: # (r1, c1)이 빈 셀인 경우
            m(r2, c2, r1, c1) # 순서만 바꾸면 됨.

    def unmerge(self, r, c):
        # 병합된 셀이 값을 가지고 있는 경우: 그 값을 (r,c)에만 주고 나머지는 빈 문자열로 채움
        val = self.cells[r][c]
        for loc in self.merged[(r, c)]:
            if loc != (r, c):
                self.before_cells[loc[0]][loc[1]] = ''
                self.cells[loc[0]][loc[1]] = ''
            else:
                self.before_cells[loc[0]][loc[1]] = val
                self.cells[loc[0]][loc[1]] = val
            self.merged[loc]
    def print_cell(self, r, c):
        return 'EMPTY' if self.cells[r][c] == '' else self.cells[r][c]
        
def solution(commands):
    answer = []
    cells = cell()
    for c in commands:
        c = c.split()
        if 'UPDATE' == c[0]:
            if len(c) == 4:
                cells.update1(int(c[1]), int(c[2]), c[3])
            else:
                cells.update2(c[1], c[2])
        elif 'MERGE' == c[0]:
            cells.merge(int(c[1]), int(c[2]), int(c[3]), int(c[4]))
        elif 'UNMERGE' == c[0]:
            cells.unmerge(int(c[1]), int(c[2]))
        elif 'PRINT' == c[0]:
            answer.append(cells.print_cell(int(c[1]), int(c[2])))
    return answer

print(solution([
    "UPDATE 1 1 a", 
    "UPDATE 1 2 b", 
    "UPDATE 2 1 c", 
    "UPDATE 2 2 d", 
    "MERGE 1 1 1 2", 
    "MERGE 2 2 2 1", 
    "MERGE 2 1 1 1", 
    "PRINT 1 1", 
    "UNMERGE 2 2", 
    "PRINT 1 1"
    ]))

"""
표 크기: 50 by 50 (고정)
    초기 셀은 비어 있음(빈 문자열)
    다른 셀과 병합 가능
"UPDATE r c value"
1. (r, c) 위치의 셀 선택
2. 셀의 값을 value로
"UPDATE value1 value2"
1. value1 값을 갖는 모든 셀 탐색
2. value1 값의 셀들을 value2로 바꾸기
"MERGE r1 c1 r2 c2"
1. (r1, c1) 위치의 셀과 (r2, c2) 위치의 셀을 선택하여 병합
    - (r1, c1) == (r2, c2) -> 명령 무시
    - 인접하지 않을 수 있음 -> 해당 셀들만 영향 받음
2. 두 셀 중 한 셀이 값을 가지고 있을 경우
    - 병합된 셀은 그 한 셀의 값으로 변경
3. 두 셀 모두 값을 가짐
    - (r1, c1) 위치의 셀 값으로 변경
4. (r1, c1) 와 (r2, c2) 중 어느 위치를 선택하여도
    - 병합된 셀로 접근 -> dict로 구현
"UNMERGE r c"
1. (r, c) 위치의 셀을 선택하여 해당 셀의 모든 병합을 해제
2. 선택한 셀이 포함하고 있던 모든 셀 -> 빈 문자열로 변경
    - if 병합 직전에 값을 가지는 경우: 그 이전 값으로 변경 (즉 이전 값을 저장하고 있어야함)
    - else: 빈 문자열로 변경
"PRINT r c"
1. (r, c) 위치의 셀을 선택하여 셀의 값을 출력
2. 선택한 셀이 빈 문자열인 경우: "EMPTY"를 출력
"""