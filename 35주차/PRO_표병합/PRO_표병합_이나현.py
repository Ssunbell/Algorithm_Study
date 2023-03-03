#union & find 알고리즘
#root 노드를 기준으로 값을 넣어줬습니다.
#자식노드에 값을 update 해줘도 root 노드에 값이 update 하도록하였습니다.
#값을 찾을 때도 root 노드로 찾습니다.

def update(r,c,value):
    global table
    root_r, root_c = find(r, c)
    for i in range(51):
        for j in range(51):
            if find(i,j) == [root_r, root_c]:
                table[i][j] = value

def v1_to_v2(value1, value2):
    global table
    for i in range(51):
        for j in range(51):
            if table[i][j] == value1:
                table[i][j] = value2

def find(r, c):
    global parent
    if parent[r][c] != [r,c]:
        parent_r, parent_c = parent[r][c]
        parent[r][c] =  find(parent_r, parent_c)
    return parent[r][c]


def merge(r1,c1,r2,c2):
    global parent
    if find(r1,c1) != find(r2,c2):
        if [r1,c1] <= [r2,c2]:
            root_r2, root_c2 = find(r2,c2)
            parent[root_r2][root_c2] = find(r1,c1)
        else:
            root_r1, root_c1 = find(r1,c1)
            parent[root_r1][root_c1] = find(r2,c2)
    find(r1,c1)
    find(r2,c2)


def unmerge(root_r, root_c):
    global parent, table
    for i in range(51):
        for j in range(51):
            if parent[i][j] == [root_r, root_c]:
                parent[i][j] = [i, j]
                table[i][j] = ""

def solution(commands):
    global table, parent
    table = [[""] * 51 for _ in range(51)]
    parent = [[[i,j] for j in range(51)] for i in range(51)]
    answer = []
    for command in commands:
        command = command.split()
        if command[0] == 'UPDATE' and len(command) == 4:
            _, r, c, value = command
            r, c = int(r), int(c)
            update(r, c, value)
        elif command[0] == 'UPDATE' and len(command) == 3:
            _, value1, value2 = command
            v1_to_v2(value1, value2)
        elif command[0] == 'MERGE':
            _, r1, c1, r2, c2 = command
            r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
            root_r1, root_c1 = find(r1, c1)
            root_r2, root_c2 = find(r2, c2)
            value1 = table[root_r1][root_c1]
            value2 = table[root_r2][root_c2]
            if value1:
                update(r2,c2,value1)
            elif value2:
                update(r1,c1,value2)
            merge(r1, c1, r2, c2)
        elif command[0] == 'UNMERGE':
            _, r, c = command
            r, c = int(r), int(c)
            root_r, root_c = find(r, c)
            value = table[root_r][root_c]
            unmerge(root_r, root_c)
            table[r][c] = value
        else:
            _, r, c = command
            r, c = int(r), int(c)
            root_r, root_c = find(r, c)
            value = table[root_r][root_c]
            answer.append(value) if value else answer.append("EMPTY")
    return answer

print(solution(["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "UPDATE 5 5 E", "UPDATE 6 6 F", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 5 5 6 6", "MERGE 3 3 1 1", "MERGE 6 6 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4", "PRINT 5 5", "PRINT 6 6"]))
# print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
# print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
