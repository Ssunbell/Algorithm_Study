import sys
sys.setrecursionlimit(10**8)

input = lambda : sys.stdin.readline().strip()
        
def find_parent(node):
    if node != network[node]:
        network[node] = find_parent(network[node])
    
    return network[node]

def find_union(friend1, friend2):
    parent1 = find_parent(friend1)
    parent2 = find_parent(friend2)

    ## parent1이 Root라는 가정
    if parent2 != parent1:
        network[parent2] = parent1
        number[parent1] += number[parent2]

n = int(input())
for _ in range(n):
    network = {}
    number = {}
    
    F = int(input())
    friend_list = [input().split() for _ in range(F)]
    root1, root2 = friend_list[0]
    for row in friend_list:
        friend1, friend2 = row
        if friend1 not in network:
            network[friend1] = friend1
            number[friend1] = 1
        if friend2 not in network:
            network[friend2] = friend2
            number[friend2] = 1
            
        find_union(friend1, friend2)
        print(number[find_parent(friend1)])
            
            
## count 매서드 사용시 시간초과남
# print(list(network.values()).count(root1)+list(network.values()).count(root2))
            