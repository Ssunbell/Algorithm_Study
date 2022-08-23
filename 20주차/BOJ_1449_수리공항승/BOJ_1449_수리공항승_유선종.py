import sys
import math

input = lambda: sys.stdin.readline().strip()

n, l = map(int, input().split())
leakage = sorted(list(map(int, input().split())))

start = leakage[0]-0.5
end = start + l
answer = 1
for i in range(len(leakage)):
  if leakage[i] > end:
    answer += 1
    start = leakage[i]-0.5
    end = start + l

print(answer)