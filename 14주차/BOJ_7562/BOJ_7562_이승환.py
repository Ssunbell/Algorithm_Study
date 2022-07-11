from collections import deque
import sys 

input_s = lambda : sys.stdin.readline().strip()
t = int(input_s())

for _ in range(t):
    m = int(input_s())
    root = tuple(map(int,input_s().split()))
    dest = tuple(map(int,input_s().split()))

    dx = [1,2, 1, 2,-1,-2,-1,-2]
    dy = [2,1,-2,-1, 2, 1,-2,-1]

    q = deque()
    depth_chart = [[0]*m for _ in range(m)]
    depth_chart[root[0]][root[1]] = 0
    
    if root == dest:
        result = 0
    else:
        q.append(root)

    while q:
        x,y = q.popleft()

        if (x,y) == dest:
            break

        for i in range(8):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_y < 0 or next_x >= m or next_y >= m:
                continue
            if depth_chart[next_x][next_y] != 0:
                continue
            # if next not in q:  
            # not in 연산이 엄청 느리기 때문에 이걸 안하면 시간은 빨라진다.
            # 왜 큐에 있는지 없는지 검사를 안해도 되냐면 체스판이기 때문에 갔던곳을 또 갈 수 있기 때문이다.
            q.append((next_x,next_y))
            depth_chart[next_x][next_y] = depth_chart[x][y] + 1
    
    result =  depth_chart[dest[0]][dest[1]]

    print(result)