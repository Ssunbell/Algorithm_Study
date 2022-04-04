n = int(input())

coordinate = [tuple(map(int, input().split())) for i in range(n)]
coordinate.sort()
for row in coordinate:
    print(*row)
