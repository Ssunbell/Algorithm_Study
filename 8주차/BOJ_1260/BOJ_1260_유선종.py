import sys

input = lambda : sys.stdin.readline().strip()

n, m, v = map(int,input().split())
tree=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
tree = [sorted(l) for l in tree]
visited = [False] * (n+1)
def dfs(tree, root, visited):
    print(root, end = " ")
    visited[root] = True
    for node in tree[root]:
        if not visited[node]:
            dfs(tree, node, visited)

dfs(tree, v, visited)
print()

dp = []
visited = [False] * (n+1)
def bfs(tree, root, visited):
    dp.append(root)
    visited[root] = True
    
    while dp:
        root = dp.pop(0)
        print(root, end=" ")
        
        for node in tree:
            if root in node:
                node.remove(root)
                node.sort()
                
        if len(tree[root]) > 0:
            for node in tree[root]:
                if not visited[node]:
                    dp.append(node)
                    visited[node] = True
bfs(tree, v, visited)

'''
dfs
[[], [2,3,4], [1,4], [1,4], [1,2,3]]
현재의 루트는 1
1. 인덱스 1번 들어가서 첫번째 2 출력 후 2 방문처리
2. 인덱스 2번 들어가서 첫번째 1은 루트이므로 건너뛰고 4 출력 후 방문처리
3. 인덱스 4번 들어가서 1,4 전부 방문처리 되어있으므로 되돌아옴
4. 인덱스 2번 들어가서 1,4 전부 방문처리 되어있으므로 되돌아옴
5. 인덱스 1번 들어가서 두번째 3 출력 후 3 방문처리
6. ...

bfs
[[], [2,3,4], [1,4], [1,4], [1,2,3]]
현재의 루트는 1
1. 루트에 대한 스택을 쌓기 위해 dp에 루트를 추가
2. 저장된 스택(인덱스 0번째 숫자) 1을 꺼내서 방문처리
3. 트리에 있는 모든 1을 삭제
4. 루트 1과 연결된 노드 [2,3,4]를 dp에 차곡차곡 저장 후 방문처리
5. 다시 돌아와서 저장된 스택 2를 꺼내서 트리에 있는 2를 삭제한 뒤,
2와 연결된 노드 [4](1은 삭제함) 중에서 방문처리가 안되어 있는 숫자 dp에 차곡차곡 저장
그러나 4는 방문처리가 되어있으므로 dp에 저장 X
6. ...
''' 