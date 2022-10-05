import sys

input = sys.stdin.readline

n, m = map(int, input().split())
books = sorted(list(map(int, input().split())))
positive = []
negative = []
# positive_max = False
# negative_max = False
max_walk = 0
footprint = 0

for book in books:
    if book < 0:
        negative.append(abs(book))
    else:
        positive.append(book)
    if abs(book) > max_walk:
        max_walk = abs(book)

negative.sort(reverse=True)
positive.sort(reverse=True)

for i in range(0, len(positive), m):
    if positive[i] != max_walk:
        footprint += (positive[i] * 2)

for j in range(0, len(negative), m):
    if negative[j] != max_walk:
        footprint += (negative[j] * 2)

footprint += max_walk

print(footprint)
