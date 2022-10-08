# import sys

# input = lambda : sys.stdin.readline().strip()
# n, m = map(int, input().split())
# graph = [list(input()) for _ in range(n)]

# print(graph)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

paper = [list(input().strip()) for _ in range(n)]
print(paper)

def transpose(graph):
    col = len(graph)
    row = len(graph[0])
    graph_T = [[graph[c][r] for c in range(col)] for r in range(row)]
    yield from graph_T

paper_T = transpose(paper)
for i in paper_T:
    print(i)

def make_case(n, m):
    for i in range(2**(n*m)):
        yield bin(i)[2:].zfill(n*m)

for case in make_case(n,m):
    print(case)
    a = [list(map(int, case[row*m:row*m+m])) for row in range(n)]
    b = [list(map(int, case[col*n:col*n+n])) for col in range(m)]
    print(a)
    print(b)

# def cut_graph(case):
#     '''
#     경우의 수 중에서 0일 경우 가로로 계산,
#     1일 경우 세로로 계산
#     가로로 계산할때는 raw_data,
#     세로로 계산할때는 transpose
#     '''
#     hor = [[case[:m:m]] for _ in range(n)]
    