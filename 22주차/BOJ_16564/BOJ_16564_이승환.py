n, k = map(int,input().split())
t = list(int(input()) for _ in range(n))

start = min(t)
end = max(t) + k

while True:
    