n = int(input())

storage = [tuple(input().split()) for _ in range(n)]
storage.sort(key=lambda x:(int(x[0]), int(x[1])))

for i in storage:
    print(i[0], i[1])