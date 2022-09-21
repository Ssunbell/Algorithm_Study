n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    tree[data] = [left_node, right_node] # 딕셔너리 형태를 key 루트 : value 왼쪽 자식, 오른쪽 자식
print(tree)

# 전위 순회(Predorder Traversal)
def pre_order(node):
    if node != '.':
        print(node, end = '') # 1. 자기 자신 노드
        pre_order(tree[node][0]) # 2. 왼쪽 자식 노드
        pre_order(tree[node][1]) # 3. 오른쪽 자식 노드

# 중위 순회(Inorder Traversal)
def in_order(node):
    if node != '.':
        in_order(tree[node][0]) # 1. 왼쪽 자식 노드
        print(node, end = '') # 2. 자기 자신 노드
        in_order(tree[node][1]) # 3. 오른쪽 자식 노드

# 후위 순회(Postorder Traversal)
def post_order(node):
    if node != '.':
        post_order(tree[node][0])#  1. 왼쪽 자식 노드
        post_order(tree[node][1]) # 2. 오른쪽 자식 노드
        print(node, end = '') # 3. 자기 자신 노드

pre_order('A')
print()
in_order('A')
print()
post_order('A')