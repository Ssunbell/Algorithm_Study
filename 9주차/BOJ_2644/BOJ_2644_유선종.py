import sys

input = lambda : sys.stdin.readline().strip()

n = int(input())
x, y  = map(int,input().split())
m = int(input())

tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())  
    tree[a].append(b)
    tree[b].append(a)

answer = []
def dfs(x, depth):
    depth += 1
    visited[x] = True

    if x == y:
        return answer.append(depth)

    for i in tree[x]:
        if not visited[i]:
            return dfs(i, depth)
dfs(x, 0)
print(-1 if len(answer) == 0 else answer[0] - 1)

# tree = {}
# for _ in range(m):
#     a,b = map(int, input().split())
#     if a not in  tree.keys():
#         tree[a] = [b]
#     else:
#         tree[a].append(b)

# answer = []
# def dfs(root, depth):
#     if root == x or root == y:
#         answer.append(depth)
    
#     depth += 1
#     try:
#         siblings = tree[root]
#         for parent in siblings:
#             dfs(parent, depth)
#     except: pass

# dfs(1, 0)
# if len(answer) <2:
#     print(-1)
# else: print(sum(answer))
