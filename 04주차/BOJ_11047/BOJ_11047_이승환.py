n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

sum_coin = 0
num_coin = 0

while k != 0:
    for i in range(n-1,-1,-1):
        n_coin = k // coin[i]
        if n_coin > 0:
            k -= coin[i] * n_coin
            num_coin += n_coin
            break

print(num_coin)