import sys
sys.setrecursionlimit(10000)

input = lambda: sys.stdin.readline().strip()

m,n = map(int, input().split())
graph = [[10001] + list(map(int, input().split())) + [10001] for _ in range(m)]
graph = [[10001] * (n+2)] + graph + [[10001] * (n+2)]
dp = [[-1]*(n+2) for _ in range((m+2))]

def dfs(row, col):
    if row == m and col == n:
        return 1
    if dp[row][col] != -1:
        return dp[row][col]

    count = 0
    if graph[row-1][col] < graph[row][col]:
        count += dfs(row-1, col)

    if graph[row][col-1] < graph[row][col]:
        count += dfs(row, col-1)

    if graph[row+1][col] < graph[row][col]:
        count += dfs(row+1, col)

    if graph[row][col+1] < graph[row][col]:
        count += dfs(row, col+1)
    dp[row][col] = count

    return dp[row][col]


print(dfs(1,1))