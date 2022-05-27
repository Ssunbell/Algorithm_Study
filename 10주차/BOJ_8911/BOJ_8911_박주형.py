import sys


t = int(sys.stdin.readline())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for _ in range(t):
    order = list(map(str, sys.stdin.readline().strip()))
    direction = 0 # 북: 0 서: 1 남: 2 동: 3
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    x, y = 0, 0

    # 반복문을 통해 명령을 확인
    for i in order:
        # 명령이 "F"라면 현재 방향으로 이동
        if i == "F":
            x += dx[direction]
            y += dy[direction]

        # 명령이 "B"라면 현재 방향의 뒷 방향으로 이동
        elif i == "B":
            x -= dx[direction]
            y -= dy[direction]

        # 명령이 "L"이라면 현재 방향의 왼쪽 방향으로 변경
        # 현재 방향이 동쪽이라면 북쪽인 0으로 초기화, 다른 방향은 +1
        elif i == "L":
            if direction == 3:
                direction = 0
            else:
                direction += 1

        # 명령이 "R"이라면 현재 방향의 왼쪽 방향으로 변경
        # 현재 방향이 북쪽이라면 동쪽인 0으로 초기화, 다른 방향은 -1
        elif i == "R":
            if direction == 0:
                direction = 3
            else:
                direction -= 1

        # 거북이가 지나간 영역의 최솟값과 최대값을 구한다.
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # 거북이가 지나간 영역을 출력
    print(abs(max_x - min_x) * abs(max_y - min_y))