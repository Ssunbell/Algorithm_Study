from collections import deque

def solution(b):
    answer = 0
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    corner_dic = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
    def bfs(loc):
        cost_b = [[[1e10] * 4 for _ in range(len(b))] for _ in range(len(b))]
        if loc == 0 and b[1][0] == 0:
            cost_b[1][0][loc] = 100
            q = deque()
            q.append((1, 0, loc))
        elif loc == 3 and b[0][1] == 0:
            cost_b[0][1][loc] = 100
            q = deque()
            q.append((0, 1, loc))
        else:
            return 1e10
        while q:
            x, y, d = q.popleft()
            for i in range(4):
                xx = dx[i] + x
                yy = dy[i] + y
                if 0 <= xx < len(b) and 0 <= yy < len(b) and b[xx][yy] == 0:
                    new_cost = cost_b[x][y][d] + (600 if i in corner_dic[d] else 100)
                    if new_cost < cost_b[xx][yy][i]:
                        cost_b[xx][yy][i] = new_cost
                        q.append((xx, yy, i))
        return min(cost_b[-1][-1])

    answer = min(bfs(0), bfs(3))
    return answer