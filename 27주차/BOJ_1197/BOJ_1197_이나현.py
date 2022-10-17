#[최소 스패닝 트리]
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        parent[b] = a


V, E = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(E)]
lines.sort(key=lambda x: (x[2], x[0], x[1]))
parent = [i for i in range(V+1)]
line_cnt = 0
result = 0
for line in lines:
    if line_cnt == V - 1:
        break
    a, b, c = line
    if find_parent(a) != find_parent(b):
        line_cnt += 1
        result += c
        union(a, b)
print(result)