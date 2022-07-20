import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
n,m = map(int, input().split())

graph =[[0 for _ in range(n+1)]] + [[0] + list(map(int, input().split())) for _ in range(n)]

st = deque()
c = deque()
for i in range(n+1):
    for j in range(n+1):
        if graph[i][j] == 1:
            st.append((i,j))
        elif graph[i][j] == 2:
            c.append((i,j))

result = []
s = []
t = len(c)
chik = list(range(t))
visited = [0] * t
def dfs():
    if len(s) == m:
        result.append(tuple(s[:]))
        return
    
    for i in range(t):
        if visited[i] == 0:
            if len(s) > 0 and s[-1] > chik[i]:
                continue
            visited[i] = 1
            s.append(chik[i])
            dfs()
            visited[i] = 0
            s.pop()
dfs()

cd_min = deque()
for idx in result:
    ch = []
    for i in range(len(idx)):
        ch.append(c[idx[i]])
    tmp_list = []
    for home in st:
        tmp_dict = {}
        for i, chicken in enumerate(ch):
            distance = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
            tmp_dict[chicken] = distance
        tmp_list.append({k:v for k, v in tmp_dict.items() if min(tmp_dict.values()) == v})
    cd_min.append(tmp_list)

min_result = []
for case in cd_min:
    cnt = 0
    for c in case:
        cnt += c[next(iter(c))]
    min_result.append(cnt)
print(min(min_result))