import sys
sys.setrecursionlimit(10 ** 4)
input = lambda : sys.stdin.readline().strip()

def search(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return
    
    if graph[x][y] == 0:
        return

    if graph[x][y] == 1: 
        graph[x][y] = 0

    search(x+1, y)
    search(x, y+1)
    search(x-1, y)
    search(x, y-1)
    search(x+1, y+1)
    search(x-1, y+1)
    search(x-1, y-1)
    search(x+1, y-1)





while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    result = 0
    graph = [list(map(int,input().split()))for _ in range(h)] 
    # dfs
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                search(i, j)
                result += 1 
                
    print(result)
    