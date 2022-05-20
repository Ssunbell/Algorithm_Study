import sys

input_s = lambda : sys.stdin.readline().strip()

n,m = map(int,input_s().split())
cleaner = list(map(int,input_s().split()))
places = [list(map(int,input_s().split())) for _ in range(n)]