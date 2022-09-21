n, m = map(int, input().split())

visited = [False] * (n + 1) 
arr = [] 

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True 
            arr.append(i) 
            solve(depth + 1, n, m) 
            visited[i] = False
            arr.pop()

solve(0, n, m)