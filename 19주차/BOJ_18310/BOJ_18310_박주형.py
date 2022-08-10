import sys

input = sys.stdin.readline

n = int(input())

houses = list(map(int, input().split()))
houses.sort()

if len(houses) % 2 == 0:
    print(houses[(len(houses)//2)-1])
else:
    print(houses[len(houses)//2])


# n = int(input())
# houses = list(map(int, input().split()))
# houses.sort()
# dp = [0] * max(houses)
# for i in range(len(dp)):
#     antena = 0
#     for house in houses:
#         antena += abs((i+1) - house)
#     dp[i] = antena

# answer = 1
# place = dp[0]
# for idx, j in enumerate(dp, start=1):
#     if place > j:
#         answer = idx
#         place = j
#     else:
#         pass

# print(answer)
