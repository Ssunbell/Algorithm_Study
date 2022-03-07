points = [sum(list(map(int, input().split()))) for i in range(5)]

print(points.index(max(points))+1, max(points))
