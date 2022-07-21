import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken= []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i, j])
        if city[i][j] == 1:
            house.append([i, j])

comb = list(combinations(chicken, m))

distance = []
result = []

for i in range(len(comb)):
    for h in house:
        d = []
        for j in range(m):
            d.append(abs(h[0] - comb[i][j][0]) + abs(h[1] - comb[i][j][1]))
        distance.append(min(d))

distance_sum = 0
for i in range(len(distance)):
    distance_sum += distance[i]
    if (i + 1) % len(house) == 0:
        result.append(distance_sum)
        distance_sum = 0