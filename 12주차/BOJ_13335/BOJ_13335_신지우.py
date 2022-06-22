import sys

input = lambda: sys.stdin.readline().rstrip()

n, w, l = map(int, input().split()) 
t_weight = list(map(int, input().split())) 

time = 0 
bridge_len = [0] * w 

while bridge_len:
    time += 1 
    bridge_len.pop(0) 

    if t_weight:
        if sum(bridge_len) + t_weight[0] <= l: 
            bridge_len.append(t_weight.pop(0))

        else:
            bridge_len.append(0)

print(time)