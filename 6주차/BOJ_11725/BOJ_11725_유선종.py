import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n=int(input())
node=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    node[a].append(b)
    node[b].append(a)

visited=[False]*(n+1)
storage=[0]*(n+1)
def dfs(node,root,visited):
    visited[root]=True
    for i in node[root]:
        if not visited[i]:
            storage[i]=root
            dfs(node, i, visited)
            

dfs(node,1,visited)


for i in range(2,n+1):
        print(storage[i])
        
        
'''
예시 1번 트리 구조
     1
   6   4
  3  7  2
5

이 경우에 node에 저장되는 방법은 인덱스 번호가 루트가 되고,
루트 번호에 해당하는 인덱스의 리스트 안에는 노드가 담김
[[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]
따라서 DFS로 해당 루트와 연결되어 있는 노드들을 방문하면서
방문하지 않은 노드들의 루트를 출력해주면 됨
ex) 1번 루트를 들어갈 경우 6과 4는 1번이 출력되게 storage에 4,6번 인덱스에 1을 저장
'''