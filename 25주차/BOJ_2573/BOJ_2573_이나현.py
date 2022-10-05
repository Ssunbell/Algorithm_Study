#[빙산]
import sys
import copy
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
def get_near_sea_cnt(i, j):
    global N, M
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    cnt = 0
    for k in range(4):
        if 0 <= i+di[k] < N and 0 <= j+dj[k] < M:
            if before[i+di[k]][j+dj[k]] == 0:
                cnt += 1
    return cnt


def dfs(i, j):
    visited[i][j] = True
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for k in range(4):
        if 0 <= i+di[k] < N and 0 <= j+dj[k] < M:
            if visited[i+di[k]][j+dj[k]] == False and after[i+di[k]][j+dj[k]]:
                dfs(i+di[k], j+dj[k])
    return


N, M = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(N)]
after = [[0]*M for _ in range(N)]
year = 1

while True:
    #빙산 녹이기
    for i in range(N):
        for j in range(M):
            if before[i][j] > 0:
                sea_cnt = get_near_sea_cnt(i, j)
                after[i][j] = max(0, before[i][j] - sea_cnt)
    #하나의 빙산덩어리 탐색
    visited = [[False if after[i][j] else True for j in range(M)] for i in range(N)] #숫자있는 부분만 False
    break_flag = False
    for i in range(N):
        for j in range(M):
            if after[i][j] > 0:
                dfs(i, j)
                break_flag = True
                break
        if break_flag == True:
            break
    else:                             #빙산이 모조리 녹은 경우
        year = 0
        break
    #탐색되지않은 다른 빙산이 있는지 확인
    break_flag = False
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False: #탐색되지않은 다른 빙산 발견됨
                break_flag = True
                break
        if break_flag == True:         #2중반복문 탈출
            break
    if break_flag == True:             #while문 탈출
        break
    #1년 경과후 before 갱신, after 초기화
    year += 1
    before = copy.deepcopy(after)
    after = [[0]*M for _ in range(N)]
print(year)