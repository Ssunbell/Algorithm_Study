import sys
from collections import deque

input = lambda: sys.stdin.readline()

n, w, L = map(int, input().split())
list_truck = deque(list(map(int, input().split())))

time = 0
bridge = deque([0] * w)
while list_truck:
    bridge.popleft()
    if sum(bridge) + list_truck[0] <= L:
        bridge.append(list_truck.popleft())
    else:
        bridge.append(0)
    time += 1

print(time + w)