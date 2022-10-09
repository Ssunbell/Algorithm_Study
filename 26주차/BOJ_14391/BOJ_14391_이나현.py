#[종이조각]
N, M = map(int, input().split())
table = [list(map(int, list(input()))) for _ in range(N)]
result = 0
for case in range(2 ** (N*M)):
    sum = 0
    #오른쪽 병합 종이조각 더하기
    for i in range(N):
        j = 0
        while j < M:
            right_sum = 0
            index = i * M + j
            while case & (1 << index) == 0 and j < M:
                right_sum = 10 * right_sum + table[i][j]
                j += 1
                index += 1
            j += 1
            sum +=  right_sum
    #아래쪽 병합 종이조각 더하기
    for j in range(M):
        i = 0
        while i < N:
            down_sum = 0
            index = i * M + j
            while case & (1 << index) and i < N:
                down_sum = 10 * down_sum + table[i][j]
                i += 1
                index += M
            i += 1
            sum += down_sum
    result = max(result, sum)
print(result)