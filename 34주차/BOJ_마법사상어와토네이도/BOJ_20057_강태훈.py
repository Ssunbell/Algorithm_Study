import sys
from copy import deepcopy
input = sys.stdin.readline

scatter_ratio = [[0,0,2,0,0],[0,10,7,1,0],[5,0,0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
get_direction = {(0,1):0,(1,0):1,(0,-1):2,(-1,0):3,}

ratio_by_dir = [
    list(zip(*deepcopy(scatter_ratio)))[::-1],
    [t[::-1] for t in deepcopy(scatter_ratio)],
    list(zip(*deepcopy(scatter_ratio))),
    deepcopy(scatter_ratio),
]

def get_flow(n:int):
    loc = [n//2, n//2]
    yield loc
    for layer in range(1, n+1, 2):
        for _ in range(layer-2):
            loc[1] += 1
            yield loc
        for _ in range(layer-1):
            loc[0] += 1
            yield loc
        for _ in range(layer-1):
            loc[1] -= 1
            yield loc
        for _ in range(layer-1):
            loc[0] -= 1
            yield loc
        if layer == n:
            return
        loc[0] -= 1
        yield loc

def move(n, graph, p_loc, c_loc):
    px, py = p_loc
    cx, cy = c_loc
    direction = get_direction[(cx-px, cy-py)]
    scatter_value = graph[cy][cx]
    scatter_ratio = ratio_by_dir[direction]
    alpha = scatter_value

    for dx in range(-2,3):
        for dy in range(-2,3):
            scatter_x, scatter_y = cx+dx, cy+dy
            dot_scatter_ratio = scatter_ratio[dy+2][dx+2]
            if scatter_x<0 or n<=scatter_x:
                continue
            if scatter_y<0 or n<=scatter_y:
                continue
            if dot_scatter_ratio == 0:
                continue
            move_value = int(scatter_value * dot_scatter_ratio*0.01)
            alpha -= move_value
            graph[scatter_y][scatter_x] += move_value
    if 0<=2*cy-py<n and 0<=2*cx-px<n:
        graph[2*cy-py][2*cx-px] += alpha

    graph[cy][cx] = 0

    for l in graph:
        print(l)
    print(alpha)

    return graph
    

def solution(n, graph):
    seq = [deepcopy(i) for i in get_flow(n)]
    for p_loc, c_loc in zip(seq, seq[1:]):
        move(n, graph, p_loc=p_loc, c_loc=c_loc)
        print(f"{p_loc}=>{c_loc}")
    return graph

if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    sum2d = lambda x:sum(map(sum, x))
    orig = sum2d(graph)
    print(orig - sum2d(solution(n, graph)))