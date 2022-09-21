n = int(input())
x = list(map(int,input().split()))
max_x = max(x)
x.remove(max_x)

print(max_x + sum(x) / 2)