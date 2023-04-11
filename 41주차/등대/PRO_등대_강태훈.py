from sys import setrecursionlimit
setrecursionlimit(10**6)

def dfs(tree, visited, cnode):
    if visited[cnode]:
        return 0, 0
    visited[cnode] = True
    adj_rst = [dfs(tree, visited, adj_node) for adj_node in tree[cnode]]
    return sum(map(min, adj_rst))+1, sum(list(zip(*adj_rst))[0])


def solution(n, lighthouse):
    tree = {}
    for a, b in lighthouse:
        tree[a] = tree.get(a, [])+[b]
        tree[b] = tree.get(b, [])+[a]
    return min(dfs(tree, [False]*(n+1), 1))