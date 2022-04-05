import sys
n = int(input())

stack = []

for _ in range(n):
    command = sys.stdin.readline().split() # 시간 복잡도 줄이기 위해서 

    if command[0] == 'push':
        stack.append(command[1])

    if command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        elif len(stack) > 0:
            print(stack.pop())

    if command[0] == 'size':
        print(len(stack))

    if command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        elif len(stack) > 0:
            print(0)
            
    if command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        elif len(stack) > 0:
            print(stack[-1])