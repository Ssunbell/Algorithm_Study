# 정확하게는 이해하지 못했습니다..

n = int(input())

dx = [0,-1,0,1]
dy = [1,0,-1,0] # 북 서 남 동

for i in range(n):
    pos_x = 0
    pos_y = 0
    pos_dir = 0  # 0북 1서 2남 3동
    move = list(input())
    trace = [(pos_x, pos_y)] # 거북이의 이동 경로를 담는 trace
    for j in move:
        if j == 'F':
            pos_x = pos_x + dx[pos_dir] 
            pos_y = pos_y + dy[pos_dir]
            print(trace)
            # trace = [(0, 1)] # 앞으로 이동 
        elif j == 'B':
            pos_x = pos_x - dx[pos_dir]
            pos_y = pos_y - dy[pos_dir]
            print(trace)
            # trace = [(0, -1)] # 뒤로 이동
        elif j == 'L':
            if pos_dir == 3:
                pos_dir = 0
                print(trace)
            else:
                pos_dir += 1
                print(trace)
        elif j == 'R':
            if pos_dir == 0:
                pos_dir = 3
                print(trace)
            else:
                pos_dir -= 1
                print(trace)

        trace.append((pos_x, pos_y))
    width = max(trace, key = lambda x:x[0])[0] - min(trace, key = lambda x:x[0])[0]
    height = max(trace, key = lambda x:x[1])[1] - min(trace, key = lambda x:x[1])[1]
    print(width * height)
