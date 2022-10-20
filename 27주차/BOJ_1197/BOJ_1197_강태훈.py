import sys
input = sys.stdin.readline
v, e = map(int, input().split())
link_inform = sorted([list(map(int, input().split()))
                     for _ in range(e)], key=lambda x: x[2])
parent = [i for i in range(v)]
answer = 0


def find(f):
    if f == parent[f]:
        return f
    return find(parent[f])


def union(f1, f2):
    p1, p2 = find(f1), find(f2)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2


for n1, n2, w in link_inform:
    if find(n1-1) == find(n2-1):
        continue
    union(n1-1, n2-1)
    answer += w
print(answer)
