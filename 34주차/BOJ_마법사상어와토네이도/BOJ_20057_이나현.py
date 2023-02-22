#백준 20057 마법사 상어와 토네이도

def right_index(i,j,d):
    right_i = i + direction[(d+3)%4][0]
    right_j = j + direction[(d+3)%4][1]
    return (right_i, right_j)
def forward_index(i,j,d):
    forward_i = i + direction[d][0]
    forward_j = j + direction[d][1]
    return (forward_i, forward_j)
def left_index(i,j,d):
    left_i = i + direction[(d+1)%4][0]
    left_j = j + direction[(d+1)%4][1]
    return (left_i, left_j)


def move_sand(xi,xj,d):
    global result
    yi, yj = forward_index(xi, xj, d)
    left_1i, left_1j = left_index(xi, xj, d)
    right_1i, right_1j = right_index(xi, xj, d)
    left_7i, left_7j = left_index(yi, yj, d)
    right_7i, right_7j = right_index(yi, yj, d)
    left_2i, left_2j = left_index(left_7i, left_7j, d)
    right_2i, right_2j = right_index(right_7i, right_7j, d)
    left_10i, left_10j = forward_index(left_7i, left_7j, d)
    right_10i, right_10j = forward_index(right_7i, right_7j, d)
    alpha_i, alpha_j = forward_index(yi, yj, d)
    forward_5i, forward_5j = forward_index(alpha_i, alpha_j, d)

    scatter_info = [(left_1i, left_1j, 0.01), (right_1i, right_1j, 0.01), \
                    (left_7i, left_7j, 0.07), (right_7i, right_7j, 0.07), \
                    (left_2i, left_2j, 0.02), (right_2i, right_2j, 0.02), \
                    (left_10i, left_10j, 0.1), (right_10i, right_10j, 0.1), \
                    (forward_5i, forward_5j, 0.05)]

    for si, sj, ratio in scatter_info:
        if 0 <= si < N and 0 <= sj < N:
            table[si][sj] += int(table[yi][yj] * ratio)
        else:
            result += int(table[yi][yj] * ratio)
    if 0 <= alpha_i < N and 0 <= alpha_j < N:
        table[alpha_i][alpha_j] += int(table[yi][yj] * 0.55)
    table[yi][yj] = 0


def move_tornado():
    global i, j, d
    i = i + direction[d][0]
    j = j + direction[d][1]
    left_i = i + direction[(d+1)%4][0]
    left_j = j + direction[(d+1)%4][1]
    if visited[left_i][left_j] == False:
        d = (d+1)%4



N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
i, j = N//2, N//2
direction = [(0,-1), (1,0), (0,1), (-1,0)] #왼, 아래, 오른, 위
d = 0
result = 0
while i != 0 or j != 0:
    visited[i][j] = True
    move_sand(i, j, d)
    move_tornado()

print(result)