#[행렬]
import sys
input = sys.stdin.readline


def flip(i0, j0):
    for i in range(3):
        for j in range(3):
            arr1[i0+i][j0+j] = '1' if arr1[i0+i][j0+j] == '0' else '0'


N, M = map(int, input().split())
arr1 = [list(input()) for _ in range(N)]
arr2 = [list(input()) for _ in range(N)]
count = 0
for i in range(N-3+1):
    for j in range(M-3+1):
        if arr1[i][j] != arr2[i][j]:
            flip(i, j)
            count += 1
if arr1 == arr2:
    print(count)
else:
    print(-1)