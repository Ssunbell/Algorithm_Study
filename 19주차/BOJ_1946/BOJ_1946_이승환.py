import sys
from collections import deque

t = int(input())

for test in range(t):
    input_s = input_s = lambda : sys.stdin.readline().strip()

    n = int(input_s())
    newface = deque()
    for i in range(n):
        newface.append(tuple(map(int,input_s().split())))
    newface = sorted(newface)
    pass_num = 0
    cutline = 100001
    for score in newface:
        if score[1] < cutline:
            pass_num += 1
            cutline = score[1]
    
    print(pass_num)
