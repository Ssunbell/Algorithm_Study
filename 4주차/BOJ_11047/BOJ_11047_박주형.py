n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
coins = coins[::-1]
cnt = 0
for coin in coins:
    if coin > k:
        pass
    else:
        cnt += k // coin
        k %= coin
print(cnt)
