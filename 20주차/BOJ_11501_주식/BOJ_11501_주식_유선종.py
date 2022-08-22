import sys

input = lambda: sys.stdin.readline().strip()
t = int(input())

for _ in range(t):
    a = input()
    case = list(map(int, input().split()))
    result = 0
    while case:
        max_v = max(case)
        max_idx = case.rfind(max_v)
        result += (max_v * max_idx) - sum(case[:max_idx])
        case = case[1+max_idx:]
    print(result)