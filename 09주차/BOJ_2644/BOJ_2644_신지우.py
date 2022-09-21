n = int(input()) 
a, b = map(int, input().split()) 
m = int(input()) 
graph = [[] for _ in range(n+1)] 
visited = [False] * (n+1)  
result = [] 

for _ in range(m):
    x, y = map(int, input().split())  
    graph[x].append(y)
    graph[y].append(x)

def dfs(a_num, depth):
    depth += 1 
    visited[a_num] = True 
    
    if a_num == b: 
        result.append(depth)

    for i in graph[a_num]:
        if not visited[i]:
            dfs(i, depth)

dfs(a, 0)

if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)