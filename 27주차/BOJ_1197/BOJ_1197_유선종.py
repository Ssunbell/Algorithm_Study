import sys
input = lambda :sys.stdin.readline().strip()
V, E = map(int, input().split())

edge = []
for _ in range(E):
    node1, node2, weight = map(int, input().split())
    edge.append((node1, node2, weight))

## weight가 작은 node부터 분리집합 실행
edge.sort(key=lambda x: x[-1])

parent = list(range(V + 1))

def find_parent(node):
    if node != parent[node]:
        parent[node] = find_parent(parent[node])
    
    return parent[node]

def find_union(friend1, friend2):
    parent1 = find_parent(friend1)
    parent2 = find_parent(friend2)

    ## 숫자가 작을수록 root라는 가정
    if parent2 >= parent1:
        parent[parent2] = parent1
    else:
        parent[parent1] = parent2

cnt = 0
for node1, node2, weight in edge:
    if find_parent(node1) != find_parent(node2):
        find_union(node1, node2)
        cnt += weight
        
print(cnt)