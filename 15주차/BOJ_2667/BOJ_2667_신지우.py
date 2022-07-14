import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
map = [list(map(int, input())) for _ in range(n)]

result = [] 
cnt = 0

def search(x, y):
    global cnt

    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if map[x][y] == 0:
        return

    map[x][y] = 0
    cnt += 1

    search(x+1, y)
    search(x, y+1)
    search(x-1, y)
    search(x, y-1)

for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            search(i, j)
            result.append(cnt)
            cnt = 0

print(len(result))
for i in sorted(result):
    print(i)
