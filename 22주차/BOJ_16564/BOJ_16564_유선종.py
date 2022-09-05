import sys

input = lambda : sys.stdin.readline().strip()

n, k = map(int, input().split())
x_list = sorted([int(input()) for _ in range(n)])

start, end = x_list[0], x_list[0] + k

answer = 0
while start <= end:
    mid = (start + end) // 2
    
    level = 0
    for x in x_list:
        if mid > x:
            level += (mid - x)
    
    if level <= k:
        start = mid + 1
        answer = max(mid, answer)
    else:
        end = mid - 1
print(answer)