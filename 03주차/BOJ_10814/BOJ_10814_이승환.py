N = int(input())

members = [tuple(input().split()) for _ in range(N)]

members.sort(key=lambda x:int(x[0]))

for i in range(N):
    print(" ".join(members[i]))