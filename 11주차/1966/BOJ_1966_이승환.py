import sys
from collections import deque

input_s = lambda : sys.stdin.readline().strip()
n, idx = map(int,input_s().split())
pri = list(map(int,input_s().split()))

q = deque()
