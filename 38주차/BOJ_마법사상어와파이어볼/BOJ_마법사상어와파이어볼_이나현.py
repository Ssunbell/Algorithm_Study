#백준 20056 마법사 상어와 파이어볼
N, M, K = map(int, input().split())
fireball = [list(map(int, input().split())) for _ in range(M)]
fireball = [[r-1,c-1,m,s,d] for r,c,m,s,d in fireball]
board = [[0]*(N) for _ in range(N)]
for r,c,m,_,_ in fireball:
    board[r-1][c-1] = m
direction = {k:v for k, v in enumerate([[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]])}
for k in range(K):
    new_board = [[[] for j in range(N)] for i in range(N)]
    new_fireball = []
    for ball in fireball:
        r,c,m,s,d = ball
        nr = (r + direction[d][0] * s) % N
        nc = (c + direction[d][1] * s) % N
        new_board[nr][nc].append([m,s,d])
    for i in range(N):
        for j in range(N):
            if len(new_board[i][j]) == 1:
                m,s,d = new_board[i][j][0]
                new_fireball.append([i,j,m,s,d])
            elif len(new_board[i][j]) > 1:
                sum_m, sum_s, sum_d = 0,0,[]
                for m,s,d in new_board[i][j]:
                    sum_m += m
                    sum_s += s
                    sum_d.append(d%2)
                m = sum_m // 5
                s = sum_s // len(new_board[i][j])
                d = all(sum_d) or not any(sum_d)
                if m:
                    new_fireball += [[i,j,m,s,d] for d in [0,2,4,6]] if d else [[i,j,m,s,d] for d in [1,3,5,7]]
                    new_board[i][j] = [[m,s,d] for d in [0,2,4,6]] if d else [[m,s,d] for d in [1,3,5,7]]
    fireball = new_fireball
answer = 0
for ball in fireball:
    _,_,m,_,_ = ball
    answer += m
print(answer)