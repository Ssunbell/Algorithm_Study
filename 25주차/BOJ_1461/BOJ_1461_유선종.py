n, m = map(int, input().split())
books = list(map(int, input().split()))

negative = [b for b in books if b < 0]
positive = [b for b in books if b > 0]
distance = 0
if abs(min(negative)) >= max(positive):
    negative = sorted(negative,reverse=True)
    positive = sorted(positive, reverse=True)
else:
    negative = sorted(negative)
    positive = sorted(positive)
print(positive)
print(negative)
# if len(negative) % 2 == 0:
#     for i in range(0, len(negative), 2):
#         print(negative[i])
#         distance -= negative[i]
# else:
#     for i in range(0, len(negative), 2):
#         print(negative[i])
#         distance -= negative[i]
#     distance -= negative[-1]
# if len(positive) % 2 == 0:
#     for i in range(0, len(positive), 2):
#         distance += positive[i]
# else:
#     for i in range(0, len(positive), 2):
#         distance += positive[i]
#     distance += positive[-1]
print(distance)