from collections import defaultdict
dir = {
    0:(-1, 0), 2:(0, 1), 4:(1, 0), 6:(0, -1), 
    1:(-1, 1), 3:(1, 1), 5:(1, -1), 7:(-1, -1)
}

def single_move(info): # 상하좌우/대각선 방향 이동
    r, c, m, s, d = info
    r = ((r - 1) + dir[d][0] * s) % n + 1
    c = ((c - 1) + dir[d][1] * s) % n + 1
    return [r, c, m, s, d]

def move(fireball):
    dic = defaultdict(list)
    board = [[0] * n for _ in range(n)]
    for info in fireball:
        next_info = single_move(info) # 파이어볼 개별 이동 구현
        board[next_info[0] - 1][next_info[1] - 1] += 1
        dic[(next_info[0] - 1, next_info[1] - 1)].append(next_info)
    return board, dic

def merge(board, dic):
    fireball = list()
    target = [(i, j) for i in range(n) for j in range(n) if board[i][j] >= 2]
    for t in target:
        sum_m, sum_s, sum_d = 0, 0, list()
        num_fire = len(dic[t])
        for info in dic[t]:
            r, c, m, s, d = info
            sum_m += m
            sum_s += s
            sum_d.append(d)
        dic.pop(t) # t 위치에 있던 아이템들 초기화
        check = sum_d[0] % 2
        next_m = sum_m // 5
        next_s = sum_s // num_fire
        if next_m == 0: # 질량이 0이면 소멸
            board[t[0]][t[1]] -= 1
            continue
        for d_ in sum_d[1:]:
            if check != d_ % 2:
                next_d = [1, 3, 5, 7]
                break
        else:
            next_d = [0, 2, 4, 6]
        for d_ in next_d:
            dic[t].append([t[0] + 1, t[1] + 1, next_m, next_s, d_])
            board[t[0]][t[1]] += 4
    for loc, info in dic.items():
        fireball.extend(info)
    return fireball

if __name__ == '__main__':
    answer = 0
    n, m, k = map(int, input().split())
    fireball = [list(map(int, input().split())) for _ in range(m)]
    while(k):
        board, dic = move(fireball)
        fireball = merge(board, dic)
        k -= 1
    for info in fireball:
        answer += info[2]
    print(answer)