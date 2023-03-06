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

# from collections import deque
# from itertools import islice as slicing
# from typing import *

# N, K = map(int, input().split())
# n = deque(list(map(int, input())))

# def delete_min(n:List[int], K:int, depth:int, stack=[]):
#     if depth == 0:
#         yield stack
#     else:
#         if stack:
#             stack[-1] < 

#         yield from delete_min(n, K, depth-1, )

# print(''.join(list(map(str, next(iter(delete_min(n, K, K)))))))