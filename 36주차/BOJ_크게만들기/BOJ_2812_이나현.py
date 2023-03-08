#백준 2812 크게 만들기
N, K = map(int, input().split())
num = input()
stack = []

for new in num:
    while stack and stack[-1] < new and K:
        stack.pop()
        K -= 1
    stack.append(new)

print(''.join(stack[:-K]))


#시간초과
from collections import deque
N, K = map(int, input().split())
num = deque(input())
stack = []
erase = 0
stack.append(num.popleft())

while erase < K and num:
    new = num.popleft()
    for i in range(min(K-erase, len(stack)), -1, -1):
        if stack[-i] < new:
            for j in range(i):
                stack.pop()
            stack.append(new)
            erase += i
            break
    else:
        if len(stack) < N - K:
            stack.append(new)
print(''.join(stack+list(num)))