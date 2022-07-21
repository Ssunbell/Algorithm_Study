from collections import deque
from itertools import combinations
import sys

input_s = input_s = lambda : sys.stdin.readline().strip()

n, m = map(int,input_s().split())
city = [list(map(int,input_s().split())) for _ in range(n)]

# 모든 집을 큐에 넣음
house = deque()
chicken = deque()
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            # 치킨집이 나갈수도 있기 때문에 전부 0으로 바꿔줌
            city[i][j] = 0
            chicken.append((i,j))

# 1단계 : dfs로 모든 치킨집이 m개가 되는 모든 경우의 수를 찾음
# 포기하고 조합 라이브러리 사용
# 2단계 : bfs로 각 집의 치킨거리를 구하고 치킨거리의 합계를 구함
# 3단계 : 리스트에 저장하고 최소값 출력

# 치킨집 조합
if len(chicken) <= m:
    real_chicken = [chicken]
else:
    # 치킨집에 들어가지 못하는 애들
    real_chicken = list(combinations(chicken,m))

# 모든 치킨집의 조합만큼 탐색
# all_chicken_dist => 각 치킨집의 조합의 총 치킨거리를 저장하는 리스트
all_chicken_dist = deque()
for c in real_chicken:
    # 0으로 바뀐 자리에 치킨집을 들여보냄
    for i,j in c:
        city[i][j] = 2
    # 각 가정마다의 치킨거리를 저장하는 리스트
    chicken_dist = deque()
    q = house.copy()
    while q:
        i,j = q.popleft()
        find_cd = deque()
        visited = deque()
        depth_chart = [[0]*n for _ in range(n)]
        find_cd.append((i,j))
        di = [0,1,0,-1]
        dj = [1,0,-1,0]
        while find_cd:
            c_i, c_j = find_cd.popleft()
            visited.append((c_i,c_j))
            for k in range(4):
                n_i,n_j = c_i + di[k], c_j+dj[k]
                if n_j < 0 or n_j >= n or n_i < 0 or n_i >= n:
                    continue
                if (n_i,n_j) not in visited and (n_i,n_j) not in find_cd:
                    if city[n_i][n_j] != 2:
                        find_cd.append((n_i,n_j))
                        depth_chart[n_i][n_j] = depth_chart[c_i][c_j] + 1
                    else:
                        chicken_dist.append(depth_chart[c_i][c_j] + 1)
                        find_cd.clear()
                        break
    # 한 치킨집 조합의 모든 치킨거리를 저장
    all_chicken_dist.append(sum(chicken_dist))

    # 들어왔던 치킨집을 다시 0으로 바꿔줌
    for i,j in c:
        city[i][j] = 0

print(min(all_chicken_dist))