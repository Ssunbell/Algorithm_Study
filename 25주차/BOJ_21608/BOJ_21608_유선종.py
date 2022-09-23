import sys     

input = lambda: sys.stdin.readline().strip()
n = int(input())
student_dict = {}
for _ in range(n**2):
    row = list(map(int,input().split()))
    student, likes_list = row[0], row[1:]
    student_dict[student] = set(likes_list)
    
###  북, 남, 서, 동
dx = [-1, 1, 0, 0] # 행
dy = [0, 0, -1, 1] # 열

seat_list_2D = [[0] * n for _ in range(n)]

for student, likes_set in student_dict.items():
    dp_likes = []
    dp_empty = []
    for i in range(n): # 행
        for j in range(n): # 열
            likes, empty = 0, 0
            if seat_list_2D[i][j] == 0:
                for k in range(4): # 방향 조절
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0<=x<n and 0<=y<n:
                        if seat_list_2D[x][y] in likes_set:
                            likes += 1
                        elif seat_list_2D[x][y] == 0:
                            empty += 1
            dp_likes.append(likes)
            dp_empty.append(empty)

    max_v = max(dp_likes)
    max_count = dp_likes.count(max_v)
    if dp_likes.count(0) == n**2 and dp_empty.count(0) == n**2:
        for idx in range(n**2):
            r, c = divmod(idx, n)
            if seat_list_2D[r][c] == 0:
                seat_list_2D[r][c] = student
                break
    else:
        if max_count == 1: # 최대값이 1개만 있는 경우
            row, col = divmod(dp_likes.index(max_v), n)
            seat_list_2D[row][col] = student
            
        elif max_count > 1:
            empty_list = [(dp_empty[idx],idx) for idx, value, in enumerate(dp_likes) if value == max_v]
            empty_list.sort(key=lambda x: (-x[0], x[1]))
            row, col = divmod(empty_list[0][1],n)
            seat_list_2D[row][col] = student

answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        likes_set = student_dict[seat_list_2D[i][j]]
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0<=x<n and 0<=y<n:
                if seat_list_2D[x][y] in likes_set:
                    cnt += 1
        if cnt > 0:
            answer += 10 ** (cnt - 1)
print(answer)