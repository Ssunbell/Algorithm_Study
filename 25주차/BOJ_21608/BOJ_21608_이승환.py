n = int(input())
students = [list(map(int,input().split())) for _ in range(n*n)]

def make_classroom(n):
    '''교실을 생성
       c[i][j][0]은 ij에 앉아있는 학생,
       c[i][j][1]은 ij와 인접한 빈칸의 수,
       c[i][j][2]는 ij와 인접한 가장 좋아하는 학생의 수'''
    classroom = [ [[0,0,0] for _ in range(n)] for _ in range(n)] 
    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    for i in range(n):
        for j in range(n):
            for k in range(4):
                if 0 <= i+di[k] < n and 0 <= j+dj[k] < n:
                    classroom[i][j][1] += 1
    return classroom

def check_4(list_,favorite):
    '''가장 우선순위가 되는 빈칸을 탐색하는 함수'''
    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    max_val = [-1,-1]
    next_i, next_j = 0,0
    for i in range(n):
        for j in range(n):
            if list_[i][j][0] != 0:
                continue
            for k in range(4):
                if 0 <= i+di[k] < n and 0 <= j+dj[k] < n and list_[i+di[k]][j+dj[k]][0] in favorite:
                    list_[i][j][2] += 1
            if max_val != max(max_val,[list_[i][j][2],list_[i][j][1]]):
                next_i, next_j = i,j
                max_val = [list_[i][j][2],list_[i][j][1]]
            list_[i][j][2] = 0
    return next_i, next_j

def update_blank(i,j,student,list_):
    '''자리가 확정이 되면 정보를 업데이트 하는 함수'''
    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    list_[i][j][0] = student
    list_[i][j][1] = 0
    for k in range(4):
        if 0 <= i+di[k] < n and 0 <= j+dj[k] < n and list_[i+di[k]][j+dj[k]][1] != 0:
            list_[i+di[k]][j+dj[k]][1] -= 1
    return list_

def get_satisfaction(list_,info):
    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    score = [[0]*n for i in range(n)]
    result =0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                if 0 <= i+di[k] < n and 0 <= j+dj[k] < n:
                    if list_[i+di[k]][j+dj[k]][0] in info[list_[i][j][0]]:
                        score[i][j] += 1
            if score[i][j] == 1:
                result += 1
            elif score[i][j] == 2:
                result += 10
            elif score[i][j] == 3:
                result += 100
            elif score[i][j] == 4:
                result += 1000
    return result

def solution(n,students):
    classroom = make_classroom(n)
    st_info = [0]*((n*n)+1)
    for info in students:
        student = info[0]
        favorite = info[1:]
        st_info[student] = favorite
        i,j = check_4(classroom,favorite)
        classroom = update_blank(i,j,student,classroom)

    answer = get_satisfaction(classroom,st_info)
    return answer

print(solution(n,students))