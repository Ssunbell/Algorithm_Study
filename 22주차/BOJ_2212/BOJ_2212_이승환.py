n = int(input())
k = int(input())
# 위치를 정렬
sensors = sorted(list(map(int,input().split())))

# 각 센서들은 집중국과 연결되어야함.
# 모든 센서들이 연결되어있다고 할 때, 각 센서들의 연결점은 n-1개
# 연결점을 k-1개만큼 지우면 k개의 영역으로 분할됨
# 1개를 1번 나누면 2개, 2번나누면 3개가, 3번 나누면 4개가됨. 나누는 것이 연결점을 지우는 것.
# 가장 작은 길이를 가지는 영역으로 분할하기 위해서는 가장 긴 것 부터 지우면 됨.
# 각 센서를 연결하는 연결길이를 구하고 그것을 위에서부터 자른 뒤 합을 구하면 됨.
len_sensors = [0] * (n)
for i in range(1,n):
    len_sensors[i-1] = sensors[i] - sensors[i-1]

len_sensors.sort()

print(sum(len_sensors[:n-k+1]))
