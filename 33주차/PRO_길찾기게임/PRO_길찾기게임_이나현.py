#[프로그래머스_길찾기게임]
# 트라이구조로 계층 표현
# 전위 순회, 후위 순회는 재귀로 찾았다.

import sys
sys.setrecursionlimit(10 ** 6)

class Trie():
    def __init__(self, x):
        self.x = x
        self.left_child = None  #왼쪽 서브트리
        self.right_child = None #오른쪽 서브트리
        
    def insert(self, insert_x):
        curr = self
        while True:
            parent_x = curr.x
            if insert_x < parent_x:
                if curr.left_child == None:
                    curr.left_child = Trie(insert_x)
                    break
                else:  
                    curr = curr.left_child
            else:
                if curr.right_child == None:
                    curr.right_child = Trie(insert_x)
                    break
                else:
                    curr = curr.right_child


def solution(nodeinfo):

    def preorder_traversal(tree):
        curr = tree
        pre_arr.append(node_name[curr.x])
        if curr.left_child:
            preorder_traversal(curr.left_child)
        if curr.right_child:
            preorder_traversal(curr.right_child)
        return

    def postorder_traversal(tree):
        curr = tree
        if curr.left_child:
            postorder_traversal(curr.left_child)
        if curr.right_child:
            postorder_traversal(curr.right_child)
        post_arr.append(node_name[curr.x])
        return


    node_name = {nodeinfo[i][0]:i+1 for i in range(len(nodeinfo))} #모든 노드는 서로다른 x를 가진다.
    nodeinfo.sort(key=lambda x: (-x[1], x[0])) #y에 대해선 내림차, x에 대해선 오름차순으로 정렬 -> 트리에 insert 순서
    tree = Trie(nodeinfo[0][0]) #맨 꼭대기노드의 트리(x)
    nodeinfo = nodeinfo[1:]

    for node in nodeinfo:
        tree.insert(node[0])
    
    pre_arr = []
    post_arr = []
    preorder_traversal(tree)
    postorder_traversal(tree)

    return [pre_arr, post_arr]

print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))