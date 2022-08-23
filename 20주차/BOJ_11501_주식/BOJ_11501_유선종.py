import sys

input = lambda: sys.stdin.readline().strip()
t = int(input())

for _ in range(t):
    a = input()
    case = list(map(int, input().split()))
    result = 0
    max_v = 0
    for i in range(len(case)-1,-1,-1):
        if case[i] > max_v:
            max_v = case[i]
        else:
            result += max_v - case[i]
    print(result)
    
# 앞에서 시작하면 시간초과 남    
    # while case:
    #     max_v = max(case)
    #     max_idx = case.index(max_v)
    #     result += (max_v * max_idx) - sum(case[:max_idx])
    #     case = case[1+max_idx:]
    # print(result)