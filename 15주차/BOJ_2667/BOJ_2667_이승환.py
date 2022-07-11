import sys
from collections import deque

input_s = input_s = lambda : sys.stdin.readline().strip()

n = int(input_s())
apt = [list(map(int,input_s())) for _ in range(n)]

# 큐에 아파트가 들어서있는 좌표 입력
q = deque()
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1:
            q.append((i,j))

# bfs
di = [0,1,0,-1]
dj = [1,0,-1,0]

apt_num = 0
apt_nums = deque()

while q:
    i,j = q.popleft()

    # 단지로 연결된 아파트를 구하기 위한 bfs
    apt_q = deque()
    apt_q.append((i,j))

    apt_num_semi = 0

    while apt_q:
        curr_i, curr_j = apt_q.popleft()

        # 방문했을 경우 1을 2로 바꿔줌
        apt[curr_i][curr_j] = 2

        # 단지 내 아파트의 수를 카운트
        apt_num_semi += 1

        for k in range(4):
            next_i = curr_i + di[k]
            next_j = curr_j + dj[k]
            next = (next_i,next_j)

            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
                continue

            # apt_q에 없고 방문하지 않은 좌표는 apt_q에 넣고 중복 방문을 막기위해 큐에서 삭제
            if next not in apt_q and apt[next_i][next_j] == 1:
                apt_q.append(next)
                q.remove(next)
    
    apt_num += 1
    apt_nums.append(apt_num_semi)

apt_nums = sorted(apt_nums)

print(apt_num)
for i in apt_nums:
    print(i)