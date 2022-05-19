# 가져온 코드

import sys
input = lambda: sys.stdin.readline().rstrip()
n = input()

move = list(input())

# 남 서 북 동 
# 여기서부터 이해 X
x = [1,0,-1,0]
y = [0,-1,0,1]
 
# 시작 위치
# 임의의 위치 0,0
temp = [[0,0]]
 
# 현재 바라보는 방향
dir = 0
 
# 현재 위치 값
i = 0
j = 0
 
for q in move:
 
    # 앞으로 이동
    if q == 'F':
        i += x[dir % 4]
        j += y[dir % 4]
        temp.append([i,j])
 
    # 오른쪽 바라보기
    elif q == 'R':
        dir += 1
 
    # 왼쪽 바라보기
    else:
        dir += 3
 
# i 와 j 따로 저장
# 길이 알아내기 위함
i_idx = []
j_idx = []
 
for w in temp:
    i_idx.append(w[0])
    j_idx.append(w[1])
 
# 길이 저장
# board의 크기 결정
i_cnt = len(set(i_idx))
j_cnt = len(set(j_idx))
 
i_min = min(i_idx)
 
# 최소 값이 0보다 작으면 abs(최소값)만큼 다 더해주기
# 시작 위치를 0으로 고정하기 위해
if i_min < 0:
    i_c = abs(i_min)
 
# 그 이상이면 변화 시킬 필요 없음
else:
    i_c = 0
 
j_min = min(j_idx)
if j_min < 0:
    j_c = abs(j_min)
else:
    j_c = 0
 
# 아까 구했던 i와 j의 길이 값을 기반으로 board 생성
visited = [[0]*j_cnt for _ in range(i_cnt)]
 
# temp에 저장된 값 돌면서 방문한 곳은 . 처리
for e in temp:
    visited[e[0]+i_c][e[1]+j_c] = '.'
 
# 방문하지 않은 곳은 벽으로 처리
for ii in range(i_cnt):
    if ii != 0:
        print()
    for jj in range(j_cnt):
        if visited[ii][jj] == 0:
            print('#',end='')
        else:
            print(visited[ii][jj],end='')