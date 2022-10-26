from collections import deque

class Node():
    def __init__(self):
        self.time = None

class Tree():
    def __init__(self):
        self.nodes = {}
        self.nodes[-1] = Node()
        self.nodes[-1].time = 0

    def find_parent(self,parents):
        max_val = -1
        for p in parents:
            try:
                max_val = max(self.nodes[p].time,max_val)
            except:
                return -1
        return max_val

    def tree_insert(self,name,time,p_time):
        if name not in self.nodes:
            self.nodes[name] = Node()
            self.nodes[name].time = p_time + time

n = int(input())
q = deque([[i,list(map(int,input().split()))] for i in range(1,n+1)])
# q = [[1,[10,-1]],[2,[5,1,-1]]]

bt = Tree()

while q:
    building = q.popleft()
    name,data = building
    time,parents = data[0],data[1:]
    p_time = bt.find_parent(parents)
    if p_time != -1:
        bt.tree_insert(name,time,p_time)
    else:
        q.append(building)

for i in range(1,n+1):
    print(bt.nodes[i].time)

'''
아이디어
"테크트리라는 말이 있듯이 트리 자료구조를 사용해 문제를 푼다"
어떤 건물이 완성되기 위해서는 모든 부모건물이 완성되어야한다.
총 건설 시간을 어떤 건물이 완성되기위해서 최종적으로 걸리는 시간(정답으로 요구하는 시간)이라 한다면
총 건설시간은 모든 부모 건물의 건설시간중 가장 큰값과 해당 건물 건설시간의 합.
time = 총 건설시간, my_time = 그 건물을 짓는데 걸리는 시간
즉, time = max(all_parents_time) + my_time

그래서 트리를 구성, 노드에는 총 건설시간을 저장
어떤 건물이 들어왔을때, 모든 부모노드가 있다면 
  -> 그중 건설시간이 제일 긴 부모노드를 찾아서 총 건설시간을 저장
부모노드가 하나라도 존재하지 않는다면
  -> 큐의 맨 마지막으로 보냄
'''