import sys
from collections import deque
input_s = lambda : sys.stdin.readline().strip()

n, w, l = map(int,input_s().split())
a = deque(map(int,input_s().split()))

bridge = deque()
trucks = deque()
cnt = 0
while True:
    if bridge or a:
        pass
    else:
        break

    cnt += 1

    if bridge:
        for i in range(len(trucks)):
            trucks[i] += 1
        if trucks[0] > w:
            bridge.popleft()
            trucks.popleft()
    
    if bridge and a:
        if sum(bridge) + a[0] <= l:
            bridge.append(a.popleft())
            trucks.append(1)
    elif a:
        bridge.append(a.popleft())
        trucks.append(1)

print(cnt)