import sys
input=sys.stdin.readline
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

rot90 = lambda x: [i[::-1] for i in zip(*x)]
rot270 = lambda x: [i for i in zip(*x)][::-1]
entire_reverse = lambda x: [i[::-1] for i in x]

def gravity(board):
    res = []
    for row in board:
        arr = [val for val in row if val]
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                arr[i] *= 2
                arr[i + 1] = 0
        arr = [val for val in arr if val]
        res.append(arr + [0] * (n - len(arr)))
    return res

movement=[
    lambda x: gravity(x),
    lambda x: entire_reverse(gravity(entire_reverse(x))),
    lambda x: rot270(gravity(rot90(x))),
    lambda x: rot90(gravity(rot270(x)))
]

def dfs(cnt, graph):
    if cnt == 5:
        return max(list(map(max,graph)))
    return max([dfs(cnt+1, func(graph)) for func in movement])

print(dfs(0,graph))