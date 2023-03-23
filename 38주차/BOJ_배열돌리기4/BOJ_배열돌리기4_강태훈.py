import sys
input = sys.stdin.readline

from itertools import permutations

def solve(A, queries):
    for r, c, radius in queries:
        r -= 1; c-=1
        for s in range(1, radius+1):
            ltop, rtop, lbot, rbot = A[r-s][c-s], A[r-s][c+s], A[r+s][c-s], A[r+s][c+s]
            for i in range(2*s-1):
                A[r-s+i][c-s] = A[r-s+i+1][c-s]
                A[r+s][c-s+i] = A[r+s][c-s+i+1]
                A[r+s-i][c+s] = A[r+s-i-1][c+s]
                A[r-s][c+s-i] = A[r-s][c+s-i-1]
            A[r-s][c-s+1], A[r-s+1][c+s], A[r+s-1][c-s], A[r+s][c+s-1] = ltop, rtop, lbot, rbot
    return min(map(sum, A))
                
if __name__=="__main__":
    n, m, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    queries = [list(map(int, input().split())) for _ in range(k)]
    print(min([solve([i[:] for i in A],queries_perm) for queries_perm in permutations(queries)]))
