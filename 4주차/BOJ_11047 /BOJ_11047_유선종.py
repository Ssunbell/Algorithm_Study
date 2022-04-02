n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
coin = [i for i in coin if i < k]
coin = coin[::-1]
result = 0
for value in coin:
    num = k // value
    if num > 0:
        k = k - value * num
        result += num
print(result)