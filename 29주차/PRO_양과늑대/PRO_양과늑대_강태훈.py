def solution(info, edges):
    children = [[] for _ in info]
    for a,b in edges:
        children[a].append(b)
    def dfs(sheep, wolf, cnode, path):
        wolf = wolf + 1 if info[cnode] else wolf
        sheep = sheep if info[cnode] else sheep + 1
        if sheep <= wolf:
            return 0
        _sheep = sheep
        for p in path:
            for n in children[p]:
                if n not in path:
                    path.append(n)
                    _sheep=max(_sheep, dfs(sheep, wolf, n, path))
                    path.pop()
        return _sheep
    return dfs(0,0,0,[0])

tc = [[[0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]],[[0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]]]
for c in tc:
    print(solution(*c))
    