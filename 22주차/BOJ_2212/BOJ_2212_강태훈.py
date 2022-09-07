import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
# 센서 개수가 집중국 개수 이하이면 0일 수 밖에 없음. 조기종료
if N <= K:
    print(0)
    exit()
# 따라서 정렬된 센서 위치를 통해 거리차를 구하고, 거리차를 정렬한 후 앞부터 더해감.
sensors = sorted(list(map(int, input().split())))
distance_between_sensors = sorted(
    [sensors[i+1] - sensors[i] for i in range(N-1)])
print(sum(distance_between_sensors[:N - K]))
