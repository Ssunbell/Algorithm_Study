import sys
sys.setrecursionlimit(10 ** 4)
input = lambda: sys.stdin.readline()
def find(arr):
    if arr not in q:
        return
    q.remove(arr)
    cases = [[arr[0]-1, arr[1]], [arr[0], arr[1] - 1], [arr[0] + 1, arr[1]], [arr[0], arr[1] + 1]]
    for case in cases:
        if case in q:
            find(case)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    q = [list(map(int, input().split())) for _ in range(K)]
    q.sort(key=lambda x: (x[0], x[1]))

    count = 0
    while q:

        count += 1
        find(q[0])
    print(count)
