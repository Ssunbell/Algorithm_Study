from typing import *

def split_direction(direction:List[int]) -> List[int]:
    # 3-3. 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면,
    #      방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
    direction = [d % 2 for d in direction]
    if all(direction) or not any(direction):
        return [0, 2, 4, 6]
    else:
        return [1, 3, 5, 7]

N, M, K = map(int, input().split())
fireballs:List[Tuple[int]] = [tuple(map(int, input().split())) for _ in range(M)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(K):
    mass:List[List[int]] = [[0]*N for _ in range(N)]
    speed:List[List[int]] = [[0]*N for _ in range(N)]
    visited:List[List[int]] = [[0]*N for _ in range(N)]
    direction:List[List[list]] = [[[] for _ in range(N)] for _ in range(N)]
    pos = set()
    # 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    for r, c, m, s, d in fireballs:
        nx = ((r - 1) + (dx[d] * s)) % N
        ny = ((c - 1) + (dy[d] * s)) % N
        mass[nx][ny] += m
        speed[nx][ny] += s
        visited[nx][ny] += 1
        direction[nx][ny].append(d)
        pos.add((nx, ny))

    fireballs = []
    for x, y in pos:
        # 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
        if visited[x][y] >= 2:
            m = int(mass[x][y] / 5) # 3-1. 질량은 (합쳐진 파이어볼 질량의 합)/5 이다.
            s = int(speed[x][y] / visited[x][y])  # 3-2. 속력은 (합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 갯수) 이다.
            ds = split_direction(direction[x][y])
            
            if m > 0: # 4. 질량이 0인 파이어볼은 소멸되어 없어진다.
                for d in ds: # 2-2. 파이어볼은 4개의 파이어볼로 나누어진다.
                    fireballs.append((x+1, y+1, m, s, d))
        else:
            m = mass[x][y]
            s = speed[x][y]
            d = direction[x][y][0]
            fireballs.append((x+1, y+1, m, s, d))

total = 0
for f in fireballs:
    total += f[2]
print(total)