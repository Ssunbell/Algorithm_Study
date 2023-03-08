def find(r, c):
    if parent[r][c] != (r, c):
        rr, cc = parent[r][c]
        parent[r][c] = find(rr, cc)
    return parent[r][c]

def update1(r, c, value):
    root = find(r, c) # 부모 노드 찾기
    for i in range(51):
        for j in range(51):
            if find(i, j) == root:
                cells[i][j] = value

def update2(value1, value2):
    for i in range(51):
        for j in range(51):
            if cells[i][j] == value1:
                cells[i][j] = value2

def merge(r1, c1, r2, c2):
    r1, c1 = find(r1, c1) # 부모 노드 찾기
    r2, c2 = find(r2, c2) # 부모 노드 찾기
    if (r1, c1) == (r2, c2):
        return
    parent[r2][c2] = (r1, c1) # 부모 노드는 (r1, c1)을 fix해도 상관없음.
    # 왜냐면, (r2, c2)가 자기 자신을 가리키는 상황에서,
    # (r2, c2) -> (r1, c1)이 됨.
    # 이 경우, (r2, c2)를 최상단 부모 노드로 가리키던 노드들의 최상단 부모 노드가 (r1, c1)으로 바뀜
    v = cells[r1][c1] if cells[r1][c1] != '' else cells[r2][c2]
    update1(r1, c1, v) # (r1, c1)을 최상단 부모 노드로 가지는 모든 셀들을 v로 업데이트

def unmerge(r, c):
    root = find(r, c) # 부모 노드 찾기
    v = cells[r][c]
    for i in range(51):
        for j in range(51):
            if find(i, j) == root:
                parent[i][j] = (i, j)
                cells[i][j] = ''
    cells[r][c] = v

def print_(r, c):
    return 'EMPTY' if cells[r][c] == '' else cells[r][c]

def solution(commands):
    global cells, parent
    answer = []
    cells = [[''] * 51 for _ in range(51)]
    parent = [[(r, c) for c in range(51)] for r in range(51)]
    for c in commands:
        c = c.split()
        if c[0] == 'UPDATE':
            if len(c) == 4:
                update1(int(c[1]), int(c[2]), c[3])
            elif len(c) == 3:
                update2(c[1], c[2])
        elif c[0] == 'MERGE':
            merge(int(c[1]), int(c[2]), int(c[3]), int(c[4]))
        elif c[0] == 'UNMERGE':
            unmerge(int(c[1]), int(c[2]))
        else:
            answer.append(print_(int(c[1]), int(c[2])))
    return answer

# print(solution([
#     "UPDATE 1 1 a", 
#     "UPDATE 1 2 b", 
#     "UPDATE 2 1 c", 
#     "UPDATE 2 2 d", 
#     "MERGE 1 1 1 2", 
#     "MERGE 2 2 2 1", 
#     "MERGE 2 1 1 1", 
#     "PRINT 1 1", 
#     "UNMERGE 2 2", 
#     "PRINT 1 1"
#     ]))
print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
            ))

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

# menu 0 0
# 0 0 0
# 0 0 0"UPDATE 1 1 menu"

# a b 0
# 0 0 0
# 0 0 0"UPDATE 1 2 b"

# a b 0
# c 0 0
# 0 0 0"UPDATE 2 1 c"

# a b 0
# c d 0
# 0 0 0"UPDATE 2 2 d"