#[주식]
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    sum = 0
    max_num = 0
    for i in range(N-1, 0, -1):
        max_num = max(max_num, arr[i])
        sum += max(0, max_num - arr[i-1])
    print(sum)