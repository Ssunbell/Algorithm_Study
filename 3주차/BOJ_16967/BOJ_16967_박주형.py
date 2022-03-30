h, w, x, y = map(int, input().split())

a = [[] for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h+x)]

for i in range(h):
    for j in range(w):
        if i < x:
            a[i].append(b[i][j])
        elif i == x and j < y:
            a[i].append(b[i][j])
        elif i >= x and j >= y:
            a[i].append(b[i][j] - a[i-x][j-y])
        elif i > x and j < y:
            a[i].append(b[i][j])


for i in range(len(a)):
    print(*a[i])
print()
