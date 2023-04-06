import sys
input = sys.stdin.readline
from bisect import bisect_right

def solve(trees, qs):
    bounds = []
    for tree in sorted(trees):
        if bounds and bounds[-1][1] >= tree[0]:
            pre = bounds.pop()
            tree = [min(tree+pre), max(tree+pre)]
        bounds.append(tree)
    answer = []
    s, e = zip(*bounds)
    for case in qs:
        t1, t2 = sorted([trees[i-1][0] for i in case])
        answer.append(int(e[bisect_right(s, t1)-1] >= t2))
    return answer

if __name__ == "__main__":
    n, q = map(int, input().split())
    trees = [list(map(int, input().split()))[:2] for _ in range(n)]
    qs = [list(map(int, input().split())) for _ in range(q)]
    print(*solve(trees, qs), sep="\n")