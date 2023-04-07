import sys

if __name__ == "__main__":
    n, q = map(int, input().split())
    trees = [list(map(int, input().split()))[:2] for _ in range(n)]
    qs = [list(map(int, input().split())) for _ in range(q)]