import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    t = int(input())
    stocks = list(map(int, input().split()))

    answer = 0
    max_stock = 0
    stocks = stocks[::-1]

    for stock in stocks:
        if stock > max_stock:
            max_stock = stock
        else:
            answer += max_stock - stock
    print(answer)
