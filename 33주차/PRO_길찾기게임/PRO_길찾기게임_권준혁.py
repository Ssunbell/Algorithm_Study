import sys
sys.setrecursionlimit(10**6)

class Node(object):
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.name = idx
        self.left = None
        self.right = None

def set_node(parent, child):
    # 왼쪽 자식 노드로 가능한 경우
    if parent.x > child.x:
        if parent.left == None:
            parent.left = child
        else:
            set_node(parent.left, child)
    # 오른쪽 자식 노드로 가능한 경우
    else:
        if parent.right == None:
            parent.right = child
        else:
            set_node(parent.right, child)

def run_order(answer, node, mode):
    if node == None: return
    if mode:
        answer.append(node.name)
        run_order(answer, node.left, mode)
        run_order(answer, node.right, mode)
    else:
        run_order(answer, node.left, mode)
        run_order(answer, node.right, mode)
        answer.append(node.name)
    return answer
            
from collections import defaultdict
def solution(nodeinfo):
    answer = []
    nodeinfo = sorted([node + [idx + 1] for idx, node in enumerate(nodeinfo)], key=lambda x:(-x[1], x[0]))
    nodeinfo = [Node(node[0], node[1], node[2]) for node in nodeinfo]
    root = nodeinfo[0]
    for node in nodeinfo[1:]:
        set_node(root, node)
    answer.append(run_order(list(), root, 1))
    answer.append(run_order(list(), root, 0))
    return answer