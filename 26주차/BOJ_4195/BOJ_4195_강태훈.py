import sys
input = sys.stdin.readline


def union(f1, f2):
    '''union two node`s set'''
    root1 = find(f1)
    root2 = find(f2)
    if root1 != root2:
        parent[root2] = root1
        number[root1] += number[root2]


def find(f):
    '''find ancestor node'''
    if f == parent[f]:
        return f
    root = find(parent[f])
    parent[f] = root
    return parent[f]


tc = int(input())
answer = []
for _ in range(tc):
    F = int(input())
    parent = {}
    number = {}
    for _ in range(F):
        f1, f2 = input().split()
        if f1 not in parent:
            parent[f1] = f1
            number[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            number[f2] = 1
        union(f1, f2)
        answer.append(number[find(f1)])
print(*answer, sep='\n')
