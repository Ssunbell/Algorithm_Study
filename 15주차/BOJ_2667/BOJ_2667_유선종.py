import sys

input = lambda : sys.stdin.readline().strip()

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

result = []
tmp = 0
def bfs(row, col):
    global tmp
    if row < 0 or row >= n or col < 0 or col >= n:
        return
    
    if graph[row][col] == 0:
        return
    
    if graph[row][col] == 1:
        graph[row][col] = 0
        tmp += 1
        
        bfs(row-1, col)
        bfs(row, col-1)
        bfs(row+1, col)
        bfs(row, col+1)

cnt = 0
for i in range(n):
    for j in range(n):
        bfs(i,j)
        if tmp != 0:
            result.append(tmp)
            tmp = 0
print(len(result))
for i in sorted(result):
    print(i)