#[센서]
N = int(input())
K = int(input())
sensor = list(set(list(map(int, input().split()))))
N = len(sensor)

if K >= N:
    print(0)
else:
    sensor.sort()
    distance = [0]*(N-1)
    for i in range(N-1):
        distance[i] = sensor[i+1] - sensor[i]
    distance.sort()
    print(sum(distance[:N-K]))