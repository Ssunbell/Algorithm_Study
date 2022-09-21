class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
        self.nodes = {}

    def node_connecting(self, data, left, right):
            if data not in self.nodes:
                self.nodes[data] = Node(data)
            if left == ".":
                pass
            else:
                if left not in self.nodes:
                    self.nodes[left] = Node(left)
                    self.nodes[data].left = self.nodes[left]
                else:
                    self.nodes[data].left = self.nodes[left]
            if right == ".":
                pass
            else:
                if right not in self.nodes:
                    self.nodes[right] = Node(right)
                    self.nodes[data].right = self.nodes[right]
                else:
                    self.nodes[data].right = self.nodes[right]


    def preorder(self,node,trab = []):  # 전위
        trab.append(node.data)
        if node.left != None:
            self.preorder(node.left,trab)
        if node.right != None:
            self.preorder(node.right,trab)
        return trab

    def postorder(self,node,trab = []):  # 후위
        if node.left != None:
            self.postorder(node.left,trab)
        if node.right != None:
            self.postorder(node.right,trab)
        trab.append(node.data)
        return trab

    def inorder(self,node,trab =[]):  # 중위
        if node.left != None:
            self.inorder(node.left,trab)
        trab.append(node.data)
        if node.right != None:
            self.inorder(node.right,trab)
        return trab
        
n = int(input())

bt = BinaryTree()

for _ in range(n):
    data, d_left, d_right = input().split()
    bt.node_connecting(data,d_left,d_right)

bt.root = bt.nodes["A"]

print("".join(bt.preorder(bt.root)))
print("".join(bt.inorder(bt.root)))
print("".join(bt.postorder(bt.root)))

