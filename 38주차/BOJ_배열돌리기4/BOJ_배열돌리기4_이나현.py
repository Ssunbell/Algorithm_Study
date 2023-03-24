#[배열돌리기4]
from itertools import permutations
import copy

def spin_shell(r, c, s):
    #오른쪽으로 한칸씩 이동
    tmp1 = array[r-s][c+s]
    for j in range(c+s, c-s, -1):
        array[r-s][j] = array[r-s][j-1]

    #아래로 한칸씩 이동
    tmp2 = array[r+s][c+s]
    for i in range(r+s, r-s+1, -1):
        array[i][c+s] = array[i-1][c+s]
    array[r-s+1][c+s] = tmp1

    #왼쪽으로 한칸씩 이동
    tmp3 = array[r+s][c-s]
    for j in range(c-s, c+s-1):
        array[r+s][j] = array[r+s][j+1]
    array[r+s][c+s-1] = tmp2

    #위로 한칸씩 이동
    for i in range(r-s, r+s-1):
        array[i][c-s] = array[i+1][c-s]
    array[r+s-1][c-s] = tmp3

N, M, K = map(int, input().split())
array_origin = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(K)]
answer = 50 * 100
for case in permutations(range(K), K):
    array = copy.deepcopy(array_origin)
    for k in case:
        r, c, s = commands[k]
        r, c = r-1, c-1
        for shell in range(1,s+1):
            spin_shell(r, c, shell)
    for i in range(N):
        answer = min(answer, sum(array[i]))
print(answer)