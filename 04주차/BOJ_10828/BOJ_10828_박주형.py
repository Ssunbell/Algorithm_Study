n = int(input())

program = [list(input().split()) for i in range(n)]
stack = []

for i in range(n):
    if program[i][0] == 'push':
        stack.append(program[i][1])
    if program[i][0] == 'pop':
        if not stack:
            print(int(-1))
        else:
            pop = stack.pop()
            print(pop)
    if program[i][0] == 'size':
        print(len(stack))
    if program[i][0] == 'empty':
        if len(stack) == 0:
            print(int(1))
        else:
            print(int(0))
    if program[i][0] == 'top':
        if len(stack) == 0:
            print(int(-1))
        else:
            top = stack[-1]
            print(top)

# 시간초과 해결하기 : pypy3로 올리니 시간초과 해결