n, k = map(int, input().split())

count = 0

coin_list = []

for i in range(n):
    a = int(input())
    coin_list.append(a)

for coin in coin_list[::-1]:
    count += k//coin
    k %= coin

print(count)