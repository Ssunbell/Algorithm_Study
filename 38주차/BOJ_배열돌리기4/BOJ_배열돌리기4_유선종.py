from typing import *

cases:List[int] = []
def combination(K:int, l:List[int]=[]):
    if len(l) == K:
        cases.append(l)
        return
        
    for i in range(K):
        if i in l: continue
        yield from combination(K, l + [i])
        
def rotate_array(
    array:List[List[int]],
    rotates:List[Tuple[int, int, int]],
    N:int,
    M:int
) -> List[List[int]]:
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for r, c, s in rotates:
        for i in range(1, s+1):
            x = (r-1) - i
            y = (c-1) - i
            prev_value = array[x][y]
            for direction in range(4):
                for _ in range(i*2):
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    if 0<=nx<N and 0<=ny<M:
                        tmp = array[nx][ny]
                        array[nx][ny] = prev_value
                        prev_value = tmp
                        x = nx
                        y = ny

    return min(map(sum, array))
        
if __name__=='__main__':
    N, M, K = map(int, input().split())
    array: List[List[int]] = [list(map(int, input().split())) for _ in range(N)]
    rotate_commands:List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(K)]

    list(combination(K)) # 제너레이터 객체 실행
    total = float('inf')
    for case in cases:
        value = rotate_array([a[:] for a in array], [rotate_commands[c] for c in case], N, M)
        total = min(total, value)
    print(total)