import sys
input = sys.stdin.readline

n, m = map(int, input().split())

paper = [input() for _ in range(n)]


def div_paper():
    for i in range(2**(n*m)):
        temp = list(format(i, "b").zfill(n*m))
        yield [temp[i:i+m] for i in range(0, m*n, m)]


def calc_sum(divtype):
    visited = [[False for _ in range(m)] for _ in range(n)]
    sumval = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                val = ""
                if divtype[i][j] == "0":  # 가로
                    current_j = j
                    while current_j < m and divtype[i][j] == divtype[i][current_j] and not visited[i][current_j]:
                        visited[i][current_j] = True
                        val += paper[i][current_j]
                        current_j += 1
                else:  # 세로
                    current_i = i
                    while current_i < n and divtype[i][j] == divtype[current_i][j] and not visited[current_i][j]:
                        visited[current_i][j] = True
                        val += paper[current_i][j]
                        current_i += 1
                    pass
                sumval += int(val)
    return sumval


answer = 0
for i in div_paper():
    answer = max(answer, calc_sum(i))
print(answer)
