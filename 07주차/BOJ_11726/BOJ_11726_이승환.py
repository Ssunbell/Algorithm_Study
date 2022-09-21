n = int(input())

dp = [0 for _ in range(n+1)]
dp[0] = 1

for i in range(1,n+1):
    if i == 1:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(max(dp)%10007)


# def combination(arr, r):
#     arr = sorted(arr)
#     used = [0 for _ in range(len(arr))]
#     result = []
#     def generate(chosen):
#         if len(chosen) == r:
#             result.append(chosen[:])
#             return
#         start = arr.index(chosen[-1]) + 1 if chosen else 0
#         for nxt in range(start, len(arr)):
#             if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
#                 chosen.append(arr[nxt])
#                 used[nxt] = 1
#                 generate(chosen)
#                 chosen.pop()
#                 used[nxt] = 0
#     generate([]) 
#     return result

# total = 0

# for k in range(n//2 + 1):
#     lst = [i for i in range(n-k)]
#     r = n - (k*2)
#     total += len(combination(lst,r))

# print(total)