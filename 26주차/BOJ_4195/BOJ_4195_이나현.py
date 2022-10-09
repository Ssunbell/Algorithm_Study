#[친구네트워크]
import sys
input = lambda : sys.stdin.readline().rstrip()

def find_parent(a):
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        for i in range(len(parent)):
            if parent[i] == b:
                parent[i] = a
    elif a > b:
        for i in range(len(parent)):
            if parent[i] == a:
                parent[i] = b

T = int(input())
for t in range(T):
    N = int(input())
    parent = []
    id = dict()
    index = 0
    for n in range(N):
        a, b = input().split()
        if a in id and b in id: #a, b 둘다 기존 친구
            union(id[a], id[b])
        elif a in id and b not in id:
            id[b] = index
            index += 1
            parent.append(find_parent(id[a]))
        elif a not in id and b in id:
            id[a] = index
            index += 1
            parent.append(find_parent(id[b]))
        else: #a, b 둘다 새로운 친구
            id[a] = index
            index += 1
            id[b] = index
            index += 1
            parent.append(id[a])
            parent.append(id[a])
        print(parent.count(0))