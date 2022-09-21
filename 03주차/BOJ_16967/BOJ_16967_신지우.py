h, w, x, y = map(int, input().split())

merge_matrix=[list(map(int, input().split())) for _ in range(h+x)]

a_matrix = [[0 for _ in range(w)] for _ in range(h)]
check = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if i < h and j < w:
            check[i][j] += 1
        if i+x < h and j+y < w:
            check[i+x][j+y] += 1

for i in range(h):
    for j in range(w):
        if check[i][j] == 1:
            a_matrix[i][j] = merge_matrix[i][j]
        elif check[i][j] == 2:
            a_matrix[i][j] = merge_matrix[i][j] - a_matrix[i-x][j-y]

for i in range(h):
    for j in range(w):
        print(a_matrix[i][j], end=' ')
    print()