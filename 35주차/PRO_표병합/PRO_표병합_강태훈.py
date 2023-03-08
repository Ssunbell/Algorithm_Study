parent = [i for i in range(2500)]
value = ["EMPTY" for _ in range(2500)]

def find(x):
    """ x의 부모노드 찾아줌 """
    if x != parent[x]:
        ploc = parent[x]
        parent[x] = find(ploc)
    return parent[x]

def union(x1, x2):
    """ merge """
    x1, x2 = find(x1), find(x2)
    if x1 == x2:
        return
    parent[x2] = x1
    val = value[x1] if value[x1]!="EMPTY" else value[x2]
    update_1(x1, val)
    
def update_1(x, val):
    """ x좌표의 value를 val로 업데이트 """
    head = find(x)
    for i in range(2500):
        if find(i) == head:
            value[i] = val

def update_2(v1, v2):
    """ value가 v1인 셀의 value를 v2로 """
    for i in range(2500):
        loc = find(i)
        if value[loc] == v1:
            value[loc] = v2

def unmerge(x):
    """ unmerge """
    head = find(x)
    val = value[head]
    for i in range(2500):
        if find(i) == head:
            parent[i] = i
            value[i] = "EMPTY" if i != x else value[i]

getloc = lambda x,y : 50*(int(x)-1) + (int(y)-1)

def show(board, title="", x_grid=5, y_grid=5):
    """ 디버깅용 유틸 함수. x_grid, y_grid만큼 보여줌 """
    print("-"*20+title+"-"*20)
    for idx, i in enumerate(range(0,2500,50)):
        if idx == y_grid: break
        print(board[i:i+x_grid])
    print("-"*50)

def solution(commands):
    answer = []
    for command in commands:
        cmd = command.split()
        cmd_len = len(cmd)
        if cmd[0] == "UPDATE":
            if cmd_len == 3:
                update_2(*cmd[1:])
            elif cmd_len == 4:
                r, c, v = cmd[1:]
                update_1(getloc(r,c), v)
                
        elif cmd[0] == "MERGE":
            r1, c1, r2, c2 = cmd[1:]
            loc1, loc2 = getloc(r1,c1), getloc(r2,c2)
            union(loc1, loc2)
            
        elif cmd[0] == "UNMERGE":
            loc = getloc(*cmd[1:])
            unmerge(loc)
                
        elif cmd[0] == "PRINT":
            loc = getloc(*cmd[1:])
            answer.append(value[find(loc)])
        # print(command)
        # show(value, title="value")
        # show(parent, title="parent")

    return answer

tc = [
    ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"],
    ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"],
]
for c in tc:
    print(solution(c))