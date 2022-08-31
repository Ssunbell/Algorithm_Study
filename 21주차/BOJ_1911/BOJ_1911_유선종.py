import sys
from math import ceil

input = lambda : sys.stdin.readline().strip()
N, L = map(int, input().split())

cases = sorted([tuple(map(int, input().split())) for _ in range(N)])

extra_p = 0
cnt = 0
for case in cases:
    if extra_p >= case[0]:
        plank_c = ceil((case[1] - extra_p) / L)
        extra_p = extra_p  + plank_c * L
    else:
        plank_c = ceil((case[1] - case[0]) / L)
        extra_p = case[0] + plank_c * L
        
    cnt += plank_c
print(cnt)