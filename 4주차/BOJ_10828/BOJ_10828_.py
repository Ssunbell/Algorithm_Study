n = int(input())
storage = [input() for _ in range(n)]

stack = []
for command in storage:
    if 'push' in command:
        command, num = command.split()
        stack.append(num)
    elif command == 'pop':
        try:
            temp = stack.pop()
            print(temp)
        except:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
    elif command == 'top':
        try:
            print(stack[-1])
        except:
            print(-1)
