import sys

input = lambda : sys.stdin.readline().strip()

n = int(input())
sample = list(map(int, input().split()))

m = int(input())
for _ in range(m):
    case = list(map(int, input().split()))
