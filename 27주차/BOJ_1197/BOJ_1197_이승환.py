# 프림 알고리즘으로 풀어보려했으나 시간초과로 실패
import sys
from collections import defaultdict
from heapq import *

input_s = lambda : sys.stdin.readline().strip()

v, e = map(int,input_s().split())
info = [list(map(int,input_s().split())) for _ in range(e)]

mst = 0
graph = defaultdict(list)

for n1, n2, wei in info:
    graph[n1].append((wei,n1,n2))
    graph[n2].append((wei,n2,n1))

nodes = [0]*(v+1)
nodes[n1] = 1
q = graph[n1]
heapify(q)

while q:
    wei, n1 ,n2 = heappop(q)
    if nodes[n2] == 0:
        nodes[n2] = 1
        mst+=wei
    
    for edge in graph[n2]:
        if nodes[edge[2]] == 0:
            heappush(q,edge)

print(mst)