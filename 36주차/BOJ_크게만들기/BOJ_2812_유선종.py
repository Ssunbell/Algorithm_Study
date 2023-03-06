from collections import deque

N, K = map(int, input().split())
num = list(input())
depth, stack = K, deque([])

for i in range(N):
    while depth > 0 and stack:
        number = stack.pop()
        if number >= num[i]:
            stack.append(number)
            break
        depth -= 1
    stack.append(num[i])

print(''.join(list(stack)[:N-K]))