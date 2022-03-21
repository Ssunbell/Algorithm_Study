n = int(input())
online_judge = [input().split() for i in range(n)]
result = sorted(online_judge, key=lambda online_judge: int(online_judge[0]))
for row in result:
    print(*row)
