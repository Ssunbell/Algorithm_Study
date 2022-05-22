import sys
from collections import deque

input_s = lambda : sys.stdin.readline().strip()

n, m = map(int,input_s().split())

p = [0]*n
l = [0]*n
mile = deque()
for i in range(n):
    p[i], l[i] = map(int,input_s().split())
    mile.append(list(map(int,input_s().split())))
    mile[i].sort()

my_mlie = deque()

for i in range(n):
    if p[i] < l[i]:
        my_mlie.append(1)
    else:
        for j in range(l[i]-1):
            mile[i].pop()
        comp = mile[i].pop()
        my_mlie.append(comp)

my_mlie = sorted(my_mlie)

cnt = 0
sum_mile = 0
for mm in my_mlie:
    sum_mile += mm
    if sum_mile > m:
        sum_mile -= mm
        break
    cnt += 1

print(cnt)