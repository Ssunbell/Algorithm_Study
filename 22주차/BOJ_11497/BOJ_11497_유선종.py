import sys

input = lambda : sys.stdin.readline().strip()
t = int(input())

for _ in range(t):
    n = int(input())
    Li = sorted(list(map(int, input().split())), reverse=True)
    
    distance = max(Li[0]- Li[1], Li[0]- Li[2])
    for i in range(3, len(Li)):
        distance = max(distance, Li[i-2]-Li[(i)])
    print(distance)