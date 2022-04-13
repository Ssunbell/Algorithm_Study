n = int(input())
d = [0] * (n + 1)
cards = [0] + list(map(int, input().split()))
d[1] = cards[1]
for i in range(2, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i-j] + cards[j])
print(d[n])
