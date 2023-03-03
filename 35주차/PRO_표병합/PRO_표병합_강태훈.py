class Node:
    def __init__(self, key=None, data=None, parent=None):
        self.key = key
        self.data = data
        self.parent = parent


class Table:
    def __init__(self):
        self.table = [[Node(key=(x,y), parent=(x,y)) for x in range(50)] for y in range(50)]
        
        self.show()

    def get_parent(self, x, y):
        x, y = map(int, (x,y))
    #     if not (0<=x<50 and 0<=y<50):
    #         raise("location out of bound")
        c_node = self.table[y][x]
        if c_node.key == c_node.parent:
            return (x, y)
        p_node = self.get_parent(*c_node.parent)
        c_node.parent = p_node
        return c_node.parent

    def update(self, x, y, data):
        x, y = map(int, (x,y))
        px, py = self.get_parent(x, y)
        self.table[py][px].data = data
        self.show()
    
    def update_value(self, value1, value2):
        for line in self.table:
            for cell in line:
                if cell.data == value1:
                    cell.data = value2
    
    def print(self, x, y):
        x, y = map(int, (x,y))
        px, py = self.get_parent(x, y)
        if self.table[py][px].data:
            return self.table[py][px].data
        else:
            return "EMPTY"
    
    def merge(self, r1, c1, r2, c2):
        r1, c1, r2, c2 = map(int, (r1,c1,r2,c2))
        if r1==r2 and c1==c2:
            return
        node_1 = self.table[c1][r1]
        node_2 = self.table[c2][r2]
        merge_value = None
        if bool(node_1.data)^bool(node_2.data):
            merge_value = node_1.data if node_1.data else node_2.data
        elif node_2.data and node_1.data:
            merge_value = node_1.data
        pnode, cnode = sorted([node_1.key, node_2.key])
        px, py = self.get_parent(*pnode)
        self.table[cnode[1]][cnode[0]].parent = (px, py)
        self.table[py][px].data = merge_value
        self.show()
    def unmerge(self, r, c):
        r, c = map(int, (r,c))
        px, py = self.get_parent(r, c)
        self.table[c][r].data = self.table[py][px].data
        self.table[c][r].parent = (r,c)

    def show(self, title=None):
        print("-"*50)
        print(f"{title}")
        for l in self.table:
            for dot in l:
                print(dot.data, end="\t")
            print()
        print("-"*50)
        
    

    # UPDATE, MERGE, UNMERGE, PRINT

def solution(commands):
    pd = Table()
    answer = []
    for command in commands:
        splited_cmd = command.split()
        function, value = splited_cmd[0], splited_cmd[1:]
        if function == "UPDATE":
            if len(value)==3:
                pd.update(*value)
            elif len(value)==2:
                pd.update_value(*value)
        elif function == "MERGE":
            pd.merge(*value)
        elif function == "UNMERGE":
            pd.unmerge(*value)
        elif function == "PRINT":
            answer.append(pd.print(*value))
    return answer

tc = [
    ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"],
    ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
]
for c in tc:
    print(solution(c))