n = int(input())
commands = []
for _ in range(n):
    _ = int(input())
    commands.append([tuple(com)  for com in input().split()])

print(commands)
    