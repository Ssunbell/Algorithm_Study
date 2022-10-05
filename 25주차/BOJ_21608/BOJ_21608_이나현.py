#[상어 초등학교]

#seat[i][j]의 인접한 친구, 인접한 빈자리 count하는 함수
def check_adjacent(i, j):
    global N
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    like_cnt = 0
    empty_cnt = 0
    for k in range(4):                                  #상하좌우 확인
        if 0 <= i+di[k] < N and 0 <= j+dj[k] < N:       #(0,0) ~ (N-1, N-1) 범위인지 확인
            if seat[i+di[k]][j+dj[k]] in student[1:]:   #인접한 좋아하는 친구라면
                like_cnt += 1
            elif seat[i+di[k]][j+dj[k]] == 0:           #빈자리라면
                empty_cnt += 1
    return [like_cnt, empty_cnt, i, j]
            
#입력 받기 및 자리 정보, seat 선언
N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
info = [[[0, 0, i, j] for j in range(N)] for i in range(N)] #[인접한 좋아하는 친구수, 인접한 빈자리수, i위치, j위치]
seat = [[0 for j in range(N)] for i in range(N)]            #학생들 실제 자리

#적절한 자리에 앉히기
for student in students:
    for i in range(N):
        for j in range(N):
            info[i][j] = [-1, -1, i, j]
            if seat[i][j] == 0:                   #비어있다면
                info[i][j] = check_adjacent(i, j) #인접한 좋아하는 친구 수, 인접한 빈자리 수 얻기
    one_d_info = sum(info, [])                    #2차원 info 행렬 -> 1차원 info 행렬
    one_d_info.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
    seat[one_d_info[0][2]][one_d_info[0][3]] = student[0]

#만족도 계산
like_table = dict()
for s in students:
    like_table[s[0]] = s[1:]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
result = 0
for i in range(N):
    for j in range(N):
        like = like_table[seat[i][j]]
        neighbor = []
        for k in range(4):
            if 0 <= i+di[k] < N and 0 <= j+dj[k] < N:       #(0,0) ~ (N-1, N-1) 범위인지 확인
                neighbor.append(seat[i+di[k]][j+dj[k]])
        near_like_cnt = len(set(neighbor) & set(like))
        result += 10 ** (near_like_cnt-1) if near_like_cnt > 0 else 0
print(result)

# 이렇게하면 틀립니다.
#        result += 10 ** (len(set(neighbor) & set(like)))
#print(result//10)