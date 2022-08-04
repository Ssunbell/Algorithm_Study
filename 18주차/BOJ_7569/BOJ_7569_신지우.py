# https://jobdong7757.tistory.com/m/90
# 1은 익은 토마토
# 0은 익지 않은 토마토
# -1은 토마토가 들어있지 않은 칸


from collections import deque
import sys

input = lambda: sys.stdin.readline().strip()
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
print(box)

# 익은 토마투를 큐에 넣음
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append((i, j, k, 0))

# 방향지시자
df = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

while q:
    f, x, y, days = q.popleft()
 
    # 인접위치 토마토 확인 
    for i in range(6): # 6개의 방향 돌아가면서 확인
        nf = f + df[i] 
        nx = x + dx[i]
        ny = y + dy[i]
        ndays = days + 1 # 날짜 1일씩 추가

        # 박스 영역 안인지 확인
        if 0 <= nx < n and 0 <= ny < m and 0 <= nf < h:
            # 안익은 토마토일 경우 익힘 처리 후 큐에 삽입
            if box[nf][nx][ny] == 0:
                box[nf][nx][ny] = 1
                # print(ndays)
                # print(days)
                q.append((nf, nx, ny, ndays))
 
# 익지 않은 토마토가 있을 경우 결과값 -1로 변경
for i in range(h):
    for j in range(n):
        if box[i][j].count(0) > 0:
            days = -1
            break
 
print(days)